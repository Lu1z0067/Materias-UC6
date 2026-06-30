#


import random

num_sorteado = random.randint(1, 10)
ganhou = False
vidas = 5

# o loop continua enquanto: ainda não ganhou ou ainda não morreu
while ganhou == False and vidas > 0:
    jogador = int(input("Sua jogada: "))

    # Se os números forem iguais VENCE
    if jogador == num_sorteado:
        ganhou = True # Para sair do loop é necessário a variavel ganhou se tornar TRUE e as vidas serem maior que zero.
    else:
        # ERROU
        print("Você errou!")
        vidas = vidas - 1
        if jogador > num_sorteado:
            print("O seu número está acima do secreto")
        else:
            print("O seu número está abaixo do secreto")
        
if vidas > 0:
    print("Parabéns, você acertou!")
    print(f"Number secreto: {num_sorteado}")
else:
    print("GAME OVER")    
    print(f"Number secreto: {num_sorteado}")