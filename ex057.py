generos, nomes = [], []

while True:
    nome = input("Nome: ")
    genero = input("Gênero (F/M/Outro): ").strip().upper()[0]

    if genero not in ["F", "M", "OUTRO"]:
        print("Gênero inválido. Por favor, digite 'F', 'M' ou 'Outro'.")
        continue

    nomes.append(nome)
    generos.append(genero)

    resposta = input("Digite 'P' para adicionar nova pessoa, OUTRA TECLA para listar: ").upper()

    if resposta != "P":
        break

for indice in range(len(nomes)):
    print("\nPessoa", (indice + 1))
    print("Nome:", nomes[indice].capitalize())
    print("Gênero:", generos[indice].capitalize())
    print("*-" * 10)
