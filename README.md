# Project

## Introduction

In the contemporary world, internet access has become a necessity for human beings. It is totally common for people to access news sites, social networks at any time of the day, whether to learn about the latest pronouncements of national or international politics, or to get in touch with that loved one who is far away. The fact is that the internet in addition to providing moments of fun and leisure, it is also a crucial tool for accessing information. Although it seems a trivial thing to do for people without disabilities, this simple act of seeking information can become a real complication if the person has a disability, whether physical or mental.

Thus, this project aims to assist in a minimal part of the development of software products, focusing on the web part that uses Hypertext Markup Language (HTML), so that it is possible to carry out tests, in a development environment to ensure that a minimum quantity accessibility is achieved by this product.

## Objective

Create a tool capable of carrying out accessibility tests, simple, on pages with the HTML language, that is integrated into the DevOps pipeline.


# Technology

The package was created using the python programming language on version 3 or higher

## Dependencies

The package dependencies that will be installed automatically are:
- beautifulsoup4 ~= 4.9; 
- py-w3c ~= 0.3

# Installation

para instalar e utilizar o pacote existem duas maneiras, sendo a primeira a instalacao diretamente do repositorio pip atraves do comando:
-
A segunda forma de instalacao seria a partir deste respositorio necessitando realizar o clone e instalar de forma local a partir deste comando:
-

# Use

Para utilizar o pacote voce podera chamar a funcao check_aces e passar o html como string, desta forma o pacote ira realizar todos os testes do pacote no quesito de acessibilidade alem de uma validacao estatica do html segundo a w3c, caso o usuario nao deseje rodar algumas das funcoes ele podera passar uma lista para o metodo check onde as funções listadas serao ignoradas.
Ao final o usuario recebera uma lista de objetos com os erros apontados

# License

A licenca utilizada no projeto foi a : 