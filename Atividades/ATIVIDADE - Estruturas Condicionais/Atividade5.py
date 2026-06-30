# Criar menu interativo usando IF.​

saldo = 1000

while True:
    try:


        print("\n=== Banco ===")
        print("Saldo atual (1)")
        print("Depositar (2)")
        print("Sacar (3)")
        print("Sair (4)")

        opcao = int(input("\nSelecione o número: "))
        if opcao == 1:
            print(saldo)
        elif opcao == 2:
            deposito = float(input("Digite o valor que será depositado: "))
            saldo = saldo + deposito
            print("Deposito realizado com sucesso!")
        elif opcao == 3:
            saque = float(input("Digite o valor que será sacado: "))
            if saque > saldo:
                print("Saldo negado!")
            else:
                saldo = saldo - saque
                print("Saldo realizado com sucesso!")
        elif opcao == 4:
            print("Obrigado por usar o nosso banco!")
        else:
            print("Opção inválida! Escolha entre 1 e 4.")

    except ValueError:
        print("Digite apenas números")