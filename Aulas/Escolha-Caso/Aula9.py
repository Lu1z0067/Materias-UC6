num = int(input("Digite um número: "))

match num:
    case 1: # Case -> Define os valores ou condições específicas a serem testados.
        print("Um")
    case 2:
        print("Dois")
    case _:
        print("Número inválido!") # case _: ->Funciona como o default ou senão padrão, executado quando nenhum dos casos anteriores é atendido.

print("\nVocê é maior?")

escolha = str(input("Digite sim / não: ")).lower()

match escolha:
    case "sim":
        print("Você é maior de 18")
    case "não":
        print("Você é menor")
    case _:
        print("Texto inválido!")