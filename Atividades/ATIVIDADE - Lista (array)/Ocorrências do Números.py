#Faça um programa que leia um número do usuário, e analisa quantas vezes aquele número digitado apareceu na lista.

from calendar import c


num = [1, 3, 5, 3, 7, 9, 3]

contagem = 0

print(num)
num_escolhido = int(input("Digite um número da lista: "))
for item in num:
    if item == num_escolhido:
        contagem += 1

print(contagem)
