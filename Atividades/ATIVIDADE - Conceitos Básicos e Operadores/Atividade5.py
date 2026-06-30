# Escreva um programa que receba um número real (com ponto flutuante) 
# digitado pelo usuário. O programa deve calcular e exibir na tela:
# O dobro desse número;
# O triplo desse número;
# A metade desse número.

try:
    num = float(input("Digite um número: "))
    print(f"\nO dobro desse número = {num * 2}")
    print(f"\nO triplo desse número = {num * 3}")
    print(f"\nA metade desse número = {num/2}")

except ValueError:
    print("\nApenas números")