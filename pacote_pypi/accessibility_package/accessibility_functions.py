from bs4 import BeautifulSoup
from .classes import exception, function_mapping
from py_w3c.validators.html.validator import HTMLValidator

exceptions = []
functions_mappings = []

def initialize_functions():
    functions_mappings.append(function_mapping.FunctionMapping(
        "check_alt",
        "Function responsible for check alt sccessibility tag on img html tag",
        True
    ))
    functions_mappings.append(function_mapping.FunctionMapping(
        "check_hs_hierarchy",
        "Function responsible for check hs hierarchy on html",
        True
    ))
    
def disable_functions(functions_code):
    for code in functions_code:
        for obj in functions_mappings:
            if obj.get_function_name() == code:
                obj.set_enable(False)

def check_alt_att_on_img(html_recebido: str):
    empty_alt = [] 
    soup = BeautifulSoup(html_recebido, 'html.parser')
    for tag in soup.find_all('img'):
        if(not tag.has_attr('alt')):
            exceptions.append(exception.AcessibilityException(tag,
             'Missing alt atribute on tag image'))
        elif(tag['alt'] == ''):
            exceptions.append(exception.AcessibilityException(tag,
             'Empty alt description'))


def check_hs_hierarchy(html_recebido: str):
    # todo verificar se é necessario fazer o stop case para o h6, existe h7?
    headings_tags = ['h1','h2','h3','h4','h5','h6']
    existing_tags = []
    soup = BeautifulSoup(html_recebido, 'html.parser')
    for tag in soup.find_all(True):
        if tag.name in headings_tags:
            existing_tags.append(tag)

    previous_tag = ''
    for h_tag in existing_tags:
        if previous_tag < h_tag.name:
            previous_tag = h_tag.name
        else:
            exceptions.append(exception.AcessibilityException(h_tag,
             'Wrong hierarchy of headings tags, next one should be equals or greatter than: ' + previous_tag))
            previous_tag = ''

def validade_html(html_recebido: str):
    vld = HTMLValidator()
    vld.validate_fragment(str(html_recebido))
    for error in vld.errors:
        print(error.get("message"))

def print_errors():
    for ex in exceptions:
        ex.display_tag_error()
        ex.display_type_error()
        print('\n')


def print_function_mapping():
    for func in functions_mappings:
        func.display_function_name()
        func.display_function_description()
        func.display_enable()
        print('\n')


def check_accessibility(html_recebido: str):
    initialize_functions()
    # create function to transform strings in list to disable functions
    # disable_functions(['check_alt'])
    # validade_html()
    
    for func in functions_mappings:
        if (func.get_function_name() == 'check_alt') and (func.get_is_enable() == True):
            check_alt_att_on_img(html_recebido)
        if (func.get_function_name() == 'check_hs_hierarchy') and (func.get_is_enable() == True):
            check_hs_hierarchy(html_recebido)

    if not exceptions:
        return True
    else:
        print('\n' + 'Acessibility erros/warnings' + '\n')
        print_errors()
        return False






