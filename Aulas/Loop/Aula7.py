podeEntrar = False

while podeEntrar == False:
    eh_maior = input("Você tem mais de 18 anos? sim/não -> ").lower()
    if eh_maior == "sim":
        tem_ingresso = input("Tem ingresso? sim/não -> ").lower()
        if tem_ingresso == "sim":
            podeEntrar = True
        else:
            print("infelizmento sem ingresso não dá")
    else:
        print("Num pode rapá")

    print("\n\n\n")

print("Bem vindo a festa!")