from bs4 import BeautifulSoup
from .classes import exception 

exceptions = []

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

def print_errors():
    for ex in exceptions:
        ex.display_tag_error()
        ex.display_type_error()
        print('\n')


def check_accessibility(html_recebido: str):
    check_alt_att_on_img(html_recebido)
    check_hs_hierarchy(html_recebido)
    print_errors()






