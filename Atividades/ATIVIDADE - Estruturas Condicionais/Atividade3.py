# Sistema de aprovação escolar.​

try:
    nota1 = float(input("Digite a nota da primeira avaliação: "))
    nota2 = float(input("Digite a nota da segunda avaliação: "))
    media = (nota1 + nota2)/2
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

except ValueError:
    print("Digite apenas números")