import os


def verifica_sentenciais_basicas(caminho_arquivo):
    lista_aberto = ["<"]
    lista_fechado = [">"]
    pilha = []
    arquivo = open(caminho_arquivo, 'r')

    while True:
        caractere = arquivo.read(1)
        if caractere in lista_aberto:
            if len(pilha)==0:
                pilha.append(caractere)
            else:
                return "Erro na sintaxe, 2 aberturas seguidas \n"
        elif caractere in lista_fechado:
            # salvando nesta posicao o meu index na minha lista de fechados para buscar o compativel na lista de abertos
            posicao = lista_fechado.index(caractere)
            if ((len(pilha) > 0) and 
            (lista_aberto[posicao] == pilha[len(pilha)-1])):
                pilha.pop()
            else:
                return "Erro na sintaxe, faltando abertura\n"
        if not caractere:
            if len(pilha)==0:
                return "Sintaxe correta =)\n"
            else:
                return "Erro na sintaxe, faltando fechadura \n"
    arquivo.close()

def abre_diretorios(caminho_diretorio):
    # TODO MELHORAR ESSA VERIFICACAO DE EXTENSAO
    list_extensoes_possiveis = [".html"]
    lista_arquivos_corretos = []
    for arquivo in os.listdir(caminho_diretorio):
        if arquivo.endswith(".html"):
            lista_arquivos_corretos.append(arquivo)
    return lista_arquivos_corretos

def main(caminho_diretorio):
    for arquivo in abre_diretorios(caminho_diretorio):
        print(arquivo)
        print(verifica_sentenciais_basicas(caminho_diretorio+'/'+arquivo))


caminho_diretorio = './arquivosteste'
main(caminho_diretorio)

# DEPOIS TEM QUE VERIFICAR COM /> E NAO SO O >