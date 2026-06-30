# Contexto: Uma loja de departamento deseja automatizar o cálculo de descontos 
# em seu sistema de caixa. Para isso, o sistema deve classificar o cliente com base 
# em sua idade e calcular o desconto da compra baseando-se no valor total gasto.
# Objetivo: Crie um programa que solicite ao usuário a idade e o valor total da 
# compra. Com base nesses dados, o programa deve realizar as seguintes etapas:


idade = int(input("Digite sua idade: "))
preco = float(input("Digite o valor total da compra: "))


# Classificação do Cliente:

if idade < 12:
    age = "Criança"
elif idade < 18:
    age = "Adolescente"
elif idade < 59:
    age = "Adulto"
else:
    age = "Idoso"

# Cálculo do Desconto

if preco > 500:
    valor = preco * 0.80
    desconto = 20
elif preco > 200 and preco <= 500:
    valor = preco * 0.90
    desconto = 10
elif preco > 100 and preco <= 200:
    valor = preco * 0.95
    desconto = 5
else:
    valor = preco
    desconto = "Não há desconto"

print("\n=== Dados ===")
print(f"Categoria: {age}")
print(f"Desconto amplicado: {desconto}%")
print(f"Valor total: {valor}")
