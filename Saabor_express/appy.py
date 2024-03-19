import os 
"""Biblioteca responsável por guardar informações"""
restaurantes = [{"nome" : "Matarelis" , "categoria" : "Italiano", "ativo" : True} ,
                {"nome" : "Sayuri" , "categoria" : "Japonesa" , "ativo" : False},
                {"nome" : "Sergio" , "categoria" : "Mexicano" , "ativo" : False}]


def exibir_nome_programa():
    """Função responsável por exibir o nome do programa"""
    print("""
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
      """)

def exibir_opcoes():
    """Função responsável por exibir as opções do usuario"""
    print("1. Cadastrar Restaurante\n2. Listar Restaurante\n3. Alterar estado do Restaurante\n4. Sair\n")

def finalizar_app():
    """Função responsável por finalizar o app"""
    exibir_subtitulo("Encerrando o app")

def voltar_ao_menu_principal():
    """Função responsável por voltar ao menu principal"""
    input("\nDigite uma tecla para retornar ao menu principal.")
    main()

def opcao_invalida():
    """Função responsável por mostrar uma opção invalida
    Outputs:
    - Retorna ao menu principal"""
    print("Opção inválida.\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Função responsável por mostrar os titulos
    Inputs:
    - texto: str - O texto do subtítulo"""
    os.system("cls")
    linha = "*" * len(texto)
    print (linha)
    print(texto)
    print (linha)
    print()

def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante
    Inputs :
    - Nome do restaurante (restaurante_cadastrado)
    -Categoria

    outputs:
    -Adiciona um novo restaurante a lista de restaurantes

    
    """
    exibir_subtitulo("Cadastro de restaurante")
    restaurante_cadastrado = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {restaurante_cadastrado}: ")
    dados_dos_restaurantes = {"nome": restaurante_cadastrado, "categoria": categoria, "ativo" : False}
    restaurantes.append(dados_dos_restaurantes)
    print(f"O {restaurante_cadastrado} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()

def listar_restaurante():
    """Função responsável por mostrar a lista de restaurantes e seus status
    Outputs:
    - Exibe a lista de restaurantes na tela"""
    exibir_subtitulo("Lista de Restaurantes")
    #para cada restaurante na lista restaurante mostarar o nome
    print(f"{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status")
    for restaurante_cadastrado in restaurantes:
        nome_restaurante = restaurante_cadastrado["nome"]
        categoria = restaurante_cadastrado["categoria"]
        ativo = "ativado" if restaurante_cadastrado["ativo"] else "desativado"
        print(f"-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """Função responsável por alterar o estado do restaurante(ativo ou desativo)
    Input: Digitar o nome do restaurante que deseja selecionar
   Outputs:
    - Exibe mensagem indicando o sucesso da operação
    """
    exibir_subtitulo("Alternar estado do restaurante.\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante["ativo"] else f"o restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")
    voltar_ao_menu_principal()

def exibir_escolhas():
    """Função responsável por ser o sistema que direciona para outras funções de acordo com a escolha do usuario
    Outputs:
    - Executa a opção escolhida pelo usuário"""
    try:
        escolha_usu =int(input("Escolha uma opção: "))
        if escolha_usu == 1:
            cadastrar_novo_restaurante()
        elif escolha_usu == 2:    
            listar_restaurante()
        elif escolha_usu == 3:        
            alternar_estado_restaurante()
        elif escolha_usu == 4:        
            finalizar_app()
        else:    
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    """Função responsável por organizar a ordem do codigo """
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    exibir_escolhas()

if __name__ == "__main__":
    main()