# Crie um programa que classifique:​

# ✔ Regras​

# 0 a 12 → Criança ​

# 13 a 17 → Adolescente ​

# 18 a 59 → Adulto ​

# 60+ → Idoso​

idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolecente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade inválida.")