import os

restaurantes = [{'nome':'Mistura Fina', 'categoria':'Caseira', 'ativo': True},{'nome':'Fogão de Minas', 'categoria':'Mineira', 'ativo': True},{'nome':'Bischof', 'categoria':'Churrasco', 'ativo': True} ]

def exibir_nome_do_programa():
    print("""\n
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    \n""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar restaurante')
    print('4. Sair\n')

def subtitulo(texto):
    os.system('cls')
    asterisco = '*' * len(texto)
    print(f'\n{asterisco}')
    print(texto)
    print(f'{asterisco}\n')

def retorno_menu():
    input('\nDigite uma tecla para voltar ao menu principal! ')
    main()

def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante na aplicação.
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante em restaurantes

    '''
    subtitulo('Cadastro de novos restaurantes')
    nome_novo_restaurante = input('Insira o nome do restaurante a ser cadastrado: ')
    categoria_novo_restaurante = input('\nInsira a categoria do restaurante mencionado: ')
    restaurantes.append({'nome':nome_novo_restaurante, 'categoria':categoria_novo_restaurante, 'ativo': False})
    print(f'\nO restaurante {nome_novo_restaurante} foi cadastrado com sucesso!')
    retorno_menu()

def listar_restaurantes():
    subtitulo('Listar Restaurantes')
    print(f'{'NOME DO RESTAURANTE'.ljust(32)} | {'CATEGORIA'.ljust(25)} | {'STATUS'}')
    for restaurante in restaurantes:
            print(f'- {restaurante['nome'].ljust(30)} | {restaurante['categoria'].ljust(25)} | {'ativado' if restaurante['ativo'] == True else 'desativado'}')
    print()
    retorno_menu()

def alterar_restaurante():
    subtitulo('Alterando o estado do restaurante')
    restaurante_selecionado = input('Informe o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == restaurante_selecionado:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'\nO restaurante {restaurante_selecionado} foi {'ativado' if restaurante['ativo'] == True else 'desativado'} com sucesso')
    if not restaurante_encontrado:
        print(f'\nO restaurante {restaurante_selecionado} não foi encontrado')
        
    retorno_menu()
        
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print()

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_restaurante()
        elif opcao_escolhida == 4:
            subtitulo('Finalizando o app!')
        else:
            subtitulo('Opção inválida!')
            retorno_menu()
    except:
        subtitulo('Opção inválida!')
        retorno_menu()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
