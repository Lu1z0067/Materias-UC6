
# Criando uma lista vazia
from math import prod
from turtle import pen


produtos = []

sair = False

print("Bem vindo ao Sistema de Estoque!")

# ! Repetir enquanto sair é igual a false
while sair == False:
    print("-"*20)
    print("1 - Listar Produtos")
    print("2 - Cadastrar um Novo Produto")
    print("3 - Deletar um Produto")
    print("0 - Sair do Sistema")

    opcao = input("Sua opção: ")

    # ! Escolha Caso / Math Case
    match opcao:
        # ? Colocaremos sair como verdadeiro para que quando rodar o loop ele sair.
        case "0":
            sair = True
        case "1":
            # Listar Produtos
            for p in produtos:
                print("- ", p)
            print("-"*20)
            input("Pressione enter para continuar...") # input nem sempre precisa de variável, mas geralmente ele precisa, pois para salvar uma informação do input é necessário uma variável
        case "2":
            print("Cadastrar novo Produto:")
            nome_produto = input("Nome do Produto: ")
            # A função append() adiciona um novo item em uma lista
            produtos.append(nome_produto)
        case "3":
            print("Remover Produtos:")
            nome_produto = input("Qaul deletado: ")

            if nome_produto in produtos:
                produtos.remove(nome_produto)
                print("Removido com Sucesso!")
            else:
                print(nome_produto," não existe na lista!")

            input("Pressione enter para continuar...")

