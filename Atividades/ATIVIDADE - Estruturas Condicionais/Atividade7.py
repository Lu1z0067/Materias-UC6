# Desenvolva um programa que auxilie no cálculo do Índice de Massa Corporal (IMC). O script deve solicitar ao usuário sua altura e seu peso (ambos como números reais), aplicar a fórmula correspondente e exibir o resultado final na tela

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso/altura**2

if IMC > 18.5 and IMC > 0:
    print(f"Índice de Massa Corporal = Peso Baixo")
elif IMC > 18.6 and IMC < 24.9:
    print(f"Índice de Massa Corporal = Peso Normal")
elif IMC > 25:
    print(f"Índice de Massa Corporal = Sobrepeso")
else:
    print("Valor inválido!")