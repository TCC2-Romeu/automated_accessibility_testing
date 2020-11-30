from bs4 import BeautifulSoup
from .classes import exception
from py_w3c.validators.html.validator import HTMLValidator
from joblib import Memory
import time

# Devo retirar essa variaveis globais?
location = "./cachedir"
memory = Memory(location, verbose=0)


def check_alt_att_on_img(html_recebido: str):
    exceptions_list = []
    soup = BeautifulSoup(html_recebido, "html.parser")
    for tag in soup.find_all("img"):
        if not tag.has_attr("alt"):
            exceptions_list.append(
                exception.AcessibilityException(
                    "AcessibilityException",
                    tag,
                    "Missing alt atribute on tag image",
                    tag.sourceline,
                    tag.sourcepos,
                )
            )
        elif tag["alt"] == "":
            exceptions_list.append(
                exception.AcessibilityException(
                    "AcessibilityException",
                    tag,
                    "Empty alt description",
                    tag.sourceline,
                    tag.sourcepos,
                )
            )
    return exceptions_list


def check_for_h1(html_recebido: str):
    exceptions_list = []
    soup = BeautifulSoup(html_recebido, "html.parser")
    tag = soup.find("h1")
    if tag == None:
        exceptions_list.append(
            exception.AcessibilityException(
                "AcessibilityException", "", "Missing header tag H1 on document", "", ""
            )
        )
    return exceptions_list


def check_hs_hierarchy(html_recebido: str):
    exceptions_list = []

    head_tags = {
        "h1": False,
        "h2": False,
        "h3": False,
        "h4": False,
        "h5": False,
        "h6": False,
    }
    existing_tags = []

    soup = BeautifulSoup(html_recebido, "html.parser")
    for tag in soup.find_all(True):
        if tag.name in head_tags and not any(
            tag.name in name for name in existing_tags
        ):
            existing_tags.append((tag.name, tag))

    for name, code_fragment in existing_tags:
        head_tags[name] = True
        for value in head_tags:
            if value != name:
                if head_tags[value] == False:
                    exceptions_list.append(
                        exception.AcessibilityException(
                            "AcessibilityException",
                            code_fragment,
                            "Suspected hierarchical order, consider reviewing it, Tag {} appeared first even without the existence of the {} tag".format(
                                name, value
                            ),
                            code_fragment.sourceline,
                            code_fragment.sourcepos,
                        )
                    )
            else:
                break

    return exceptions_list


def validade_html(html_recebido: str):
    # retornar do joblib a lista de erros a partir da string
    # evitar requisições para o site da w3c a toa
    # salvar em cache para evitar requisições duplicadas (joblib - cria objetos chamados memory)
    #  criar cache local no disco
    vld = HTMLValidator()
    vld.validate_fragment(str(html_recebido))
    exceptions_list = []

    for error in vld.errors:
        exceptions_list.append(
            exception.AcessibilityException(
                "StaticHTMLValidation",
                error["extract"].replace("\n", ""),
                error["message"],
                error["hiliteStart"],
                error["hiliteLength"],
            )
        )
    return exceptions_list


def map_functions():
    validade_html_cached = memory.cache(validade_html)
    functions = {
        "alt_att_check": check_alt_att_on_img,
        "contains_h1": check_for_h1,
        "headers_tag_hierarchy": check_hs_hierarchy,
        "static_validation_html": validade_html_cached,
    }
    return functions


def check_accessibility(html_recebido: str, exclude=()):
    functions_to_check = [
        fn for name, fn in map_functions().items() if name not in exclude
    ]
    exceptions = []
    for func in functions_to_check:
        exceptions.extend(func(html_recebido))
    if exceptions:
        return exceptions
