print("=== Gênero de Filme ===\nA -> Ação\nB -> Terror\nC -> Comédia\nD -> Ficção\n")

filme = str(input("Digite o número do gênero do filme escolhido: ")).lower()

match filme:
    case "a" | "z": # está " | " -> é igual ao "or", mas no case se utiliza o "|"
        print("Recomendado: John Wick")
    case "b":
        print("Recomendado: Pânico")
    case "c":
        print("Recomendado: Super Heroí o Filme")
    case "d":
        print("Recomendado: Star Wars")
    case _:
        print("Número Inválido!")