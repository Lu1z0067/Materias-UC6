# Verificar se número é positivo ou negativo.​

try:
    num = float(input("Digite um número: "))
    if num < 0:
        print("O número é negativo")
    else:
        print("O número é positivo")

except ValueError:
    print("\nDigite somente números")