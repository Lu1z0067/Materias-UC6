print("=== Status do seu pedido ===")

print("1 - novo / pendente\n2 - pago\n3 - enviado\n4 - entregue")

status = input("Digite o status do pedido: ").lower

match status:
    case "novo" | "pendente": # "|" seria o "or"
        print("Seu pedido está aguardando pagamento.")
    case "pago":
        print("Pagamento confirmado! Preparando envio.")
    case "enviado":
        print("Seu pedido já está a caminho.")
    case "entregue":
        print("Pedido finalizado.")
    case _:
        print("Status desconhecido.")