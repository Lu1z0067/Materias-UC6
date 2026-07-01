salarios = [20000, 3000, 3200, 1700, 12000, 2500]

total = 0

# ! Somaremos todos os salários
for soma in salarios:
    print(f"{total} + {soma}")
    total += soma
    print(f"Valor atual {total}")
print(f"\nSoma total: {total}")