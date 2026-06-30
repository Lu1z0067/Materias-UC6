p1 = float(input("Digite a nota da primeira avaliação: "))
p2 = float(input("Digite a nota da segunda avaliação: "))

media = (p1 + p2)/2

frequencia = int(input("\nDigite quantos dias você frequentou a escola: "))

frequencia = (frequencia/200)*100

if media >= 7 and frequencia >= 75:
    print("Aprovado")
else:
    print("Reprovado")

print("== DADOS ==\n")
print(f"Média = {media}")
print(f"Frequência = {frequencia}")