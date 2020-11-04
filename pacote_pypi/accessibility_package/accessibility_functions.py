from bs4 import BeautifulSoup
from .classes import exception, function_mapping
from py_w3c.validators.html.validator import HTMLValidator

def check_alt_att_on_img(html_recebido: str):
    exceptions_list = []
    soup = BeautifulSoup(html_recebido, 'html.parser')
    for tag in soup.find_all('img'):
        if(not tag.has_attr('alt')):
            exceptions_list.append(exception.AcessibilityException(tag,
             'Missing alt atribute on tag image'))
        elif(tag['alt'] == ''):
            exceptions_list.append(exception.AcessibilityException(tag,
             'Empty alt description'))
    return exceptions_list

def check_for_h1(html_recebido: str):
    exceptions_list = []
    soup = BeautifulSoup(html_recebido, 'html.parser')
    tag = soup.find('h1')
    if tag == None:
        exceptions_list.append(exception.AcessibilityException("On document",
                'Missing header tag H1'))
    return exceptions_list

def check_hs_hierarchy(html_recebido: str):
    # sem saltos de hs, comecar no 1 e ir pro 3
    # primeira vez que aparecer se aparece um hn ele tem que aparecer depois de um hn-1
    headings_tags = ['h1','h2','h3','h4','h5','h6']
    exceptions_list = []
    existing_tags = []
    aparicoes = []
    soup = BeautifulSoup(html_recebido, 'html.parser')
    
    for tag in soup.find_all(True):
        if tag.name in headings_tags:
            existing_tags.append((tag.name,tag))
    
    previous_tag = ''
    for h_tag in existing_tags:
        #  todo colocar esse pedaco na funcao de verificacao de h1
        # if existing_tags.count(h_tag) >= 1 and h_tag[0] == 'h1':
        #     exceptions_list.append(exception.AcessibilityException(None,
        #      'Excessive use of h1 tags, consider using other title tags'))

        if h_tag[0] not in aparicoes:
            aparicoes.append(h_tag[0])
            aparicoes.sort()
        
        if headings_tags[aparicoes.index(h_tag[0])] != aparicoes[aparicoes.index(h_tag[0])]:
            # se uma tag nunca aparecer vai dar pau
            # index out of range
            exceptions_list.append(exception.AcessibilityException(h_tag[1],
                    'This is the first appearance of the tag: ' + str(h_tag[0]) + 
                    ' and you skipped the tag: ' + str(headings_tags[aparicoes.index(h_tag[0])])))
            aparicoes.append(headings_tags[aparicoes.index(h_tag[0])])
            aparicoes.sort()

        if previous_tag == 'h6':
            # todo pensar neste caso
            pass

        if previous_tag != 'h6':
            if previous_tag != '':
                next_tag = headings_tags[headings_tags.index(previous_tag)+1]
                if next_tag != h_tag[0]:
                    exceptions_list.append(exception.AcessibilityException(h_tag[1],
                    'Title tag hierarchy error, your next tag should be greater than or equal to ' + str(next_tag)))
        previous_tag = h_tag[0]

    return exceptions_list

def validade_html(html_recebido: str):
    # melhorar funcao
    vld = HTMLValidator()
    vld.validate_fragment(str(html_recebido))
    print(html_recebido)
    print('\n')
    print('\n')

    for error in vld.errors:
        print(error["extract"])
        print(error['hiliteStart'] )
        print( error['hiliteLength'] )
        print(error["message"])

def print_errors(general_exceptions_list):
    for specific_exceptions_list in general_exceptions_list:
        for ex in specific_exceptions_list:
            if ex.code_fragment_error != None:
                print(ex.code_fragment_error)
            print(ex.error_message)
            print('\n')

def map_functions():
    functions = {
        # "fc_alt" : check_alt_att_on_img,
        # "fc_h1" : check_for_h1,
        "fc_hs_hierarchy" : check_hs_hierarchy,
        # "fc_validate_html" : validade_html,
    }
    return functions


def block_functions(mapped_functions, block_functions_list):
    allowed_functions = mapped_functions

    if block_functions_list != None:
        for func in block_functions_list:
         allowed_functions.pop(func, None)

    return allowed_functions

    
def check_accessibility(html_recebido: str, block_functions_list):
    # se receber nulo nas funções do usuário, rodar todas
    map_functions()
    functions_to_check =  block_functions(map_functions(), block_functions_list)
    exceptions = []

    for func in functions_to_check:
        exceptions.append(functions_to_check[func](html_recebido))


    if not exceptions:
        return True
    else:
        print('\n' + 'Acessibility erros/warnings' + '\n')
        print_errors(exceptions)
        return True







    # create function to transform strings in list to disable functions
    # disable_functions(['check_alt'])
    # acessibility_exceptions = check_for_h1(html_recebido) + check_alt_att_on_img(html_recebido)
    # validade_html(html_recebido)



    # validade_html(html_recebido)
    # for func in functions_mappings:
    #     if (func.get_function_name() == 'check_alt') and (func.get_is_enable() == True):
    #         check_alt_att_on_img(html_recebido)
    #     # if (func.get_function_name() == 'check_hs_hierarchy') and (func.get_is_enable() == True):
    #     #     check_hs_hierarchy(html_recebido)




