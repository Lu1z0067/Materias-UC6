from importlib import reload
import locale
from datetime import date
from math import comb
 
# Definir Localizade Brasil Opção comum em Windows
locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')
 
# 2. Obter a data de hoje
data_hoje = date.today()
 
# 3. Formatar a data para obter o nome do dia da semana em português
# %A retorna o nome completo do dia da semana (ex: "Quinta-feira")
dia_da_semana = data_hoje.strftime('%A')
 
# 4. Exibir o resultado
print(f"O dia da semana de hoje é: {dia_da_semana}")

movie = ["O Poderoso Chefão - D039","Matrix - B678","O Senhor dos Anéis - D889","Interestelar - M912","O resgate do soldado Ryan - G007"]
combos = ["Doritos + Refri Lata | COMBO-005 | R$ 15,90","Pipoca Salgada + Copo de Coca Cola | COMBO-072 | R$ 17,90","Pipoca Doce + Copo de Suco | COMBO-777 | R$ 14,90","Refil de Pipoca Salgada + 2 Recargas de Refri | COMBO-215 | R$ 25,90"]

while True:
    print("Bem vindo ao Cinema!\nFilmes em cartas:\n")
    for i in movie:
        print(i)
    print("-"*30)

    filme = input("Digite o código do filme: ").upper().strip()

    if filme == "D039" or filme == "B678" or filme == "D889" or filme == "M912" or filme == "G007":
        ingresso = int(input("Digite a quantidade de ingresso: "))
    else:
        print("Este código não existe!")
        break
    
    lanche = input("Você deseja um combo? ").lower()
    if lanche == "sim":
        for c in combos:
            print(c)
        combo = input("Digite o código do combo: ").upper()
        
        match combo:
            case "COMBO-005":
                combos.append("Doritos + Refri Lata")
                valor_c = 15.90
                break
            case "COMBO-072":
                combos.append("Pipoca Salgada + Copo de Coca Cola")
                valor_c = 17.90
                break
            case "COMBO-777":
                combos.append("Pipoca Doce + Copo de Suco")
                valor_c = 14.90
                break
            case "COMBO-215":
                combos.append("Refil de Pipoca Salgada + 2 Recargas de Refri")
                valor_c = 25.90
                break
            case _:
                print("\nCódigo Indisponível!")
    else:
        valor_c = 0
    
    if dia_da_semana == "segunda-feira" or dia_da_semana == "quarta-feira" or dia_da_semana == "sexta-feira":
        valor = ingresso * 32.50
    else:
        valor = ingresso * 36

print("Dados:")
print(f"Valor Total: {valor + valor_c}")
    

    

