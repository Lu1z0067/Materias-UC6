print(" === Dia da semana === ")
print("Caso 1 -> Domingo")
print("Caso 2 -> Segunda")
print("Caso 3 -> Terça")
print("Caso 4 -> Quarta")
print("Caso 5 -> Quinta")
print("Caso 6 -> Sexta")
print("Caso 7 -> Sabádo")

dia = int(input("Digite o dia da semana (1 a 7): "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabádo")
    case _:
        print("Dia inválido!")