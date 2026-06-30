
ingresso = 30

while True:
    print("\n=== CINEMA ===\n")
    print("ingresso custa R$ 30\nEstudantes ou Idosos, possuem desconto de 50%")

    idade = int(input("Digite a sua idade: "))
    if idade <= 18 and idade >= 1:
        try:
            carteira = str(input("Você tem a carteira de estudante: ")).lower()
            if carteira == "sim":
                ingresso = ingresso * 0.50
                print(f"Desconto de 50% aprovado, preço final {ingresso}")
        except ValueError:
            print("Digite sim ou não")
    elif idade >= 60:
        ingresso = ingresso * 0.50
        print(f"Desconto de 50% aprovado, preço final {ingresso}")
    elif idade <= 0:
        print("Idade Inválida")
        break
    pagamento = float(input("Pague o ingresso: "))
    if pagamento <= ingresso:
        print("Valor insuficiente! Retorne quando tiver o valor suficiente.")
    else:
        print("Obrigado! Tenha um bom filme.")
        break


