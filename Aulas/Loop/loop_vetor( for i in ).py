paises = ["Brasil","Fraça","Cabo Verder","Noruega","Costa do Marfim","Paraguai","Argentina","México","Equador","Japão"]

# ! Loop for é muito utilizado em 'sequencias' onde vetor é uma das sequencias
# ? Na tradução ele se chama "para"
# ! o loop funciona muito bem com vetores
# ? Aqui, usamos o operador 'in' para outra coisa
# ! 'paises' é o vetor
# ? 'pais' no singular é como cada 'item' da lista será chamado dentro do loop
for pais in paises:
    print(f"Classificado: {pais}")

print("-"*50)
print("Fim do Loop")