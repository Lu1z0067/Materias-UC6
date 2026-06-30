# Sistema de login simples.​
from time import sleep

while True:
    nome = str(input("Digite o nome do usuário: "))
    senha = str(input("Digite a senha: "))
    sleep(2)

    if nome == "Luiz" and senha == "1234":
        print("\nBem-Vindo")
        break
    else:
        print("\nNome ou senha incorreto, tendo novamente.")
