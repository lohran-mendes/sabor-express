import os

def limpar():
    os.system('cls')

def verifica_numero():
    limpar()
    numero_adicionado = int(input('Adicione um número: '))
    if (numero_adicionado % 2) == 0:
        print('O número adicionado é par!')
    else:
        print('O número adicionado é ímpar!')
    
def verifica_idade():
    limpar()
    idade_usuario = int(input('Insira aqui a sua idade: '))
    if idade_usuario >= 0:
        if idade_usuario <= 12 & idade_usuario >= 0:
            print('O usuário é uma criança.')
        elif idade_usuario <= 18:
            print('O usuário é um adolescente.')
        else:
            print('O usuário já é um adulto.')
    else:
        print('sua idade não é valida')

verifica_idade()