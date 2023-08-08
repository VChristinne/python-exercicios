from statistics import mean

nomes, idades, generos = [], [], []

while True:
    nomes.append(input("Nome: "))
    idades.append(int(input("Idade: ")))
    generos.append(input("Gênero: "))
    resposta = input("Digite 'P' para adicionar nova pessoa, OUTRA TECLA para listar: ").upper()

    if resposta != "P":
        break

media = mean(idades)
indice_mais_velho = idades.index(max(idades))
nome_mais_velho = nomes[indice_mais_velho]
indice_mais_novo = idades.index(min(idades))
nome_mais_novo = nomes[indice_mais_novo]

for indice in range(0, len(nomes)):
    print("\nPessoa ", (indice+1))
    print("Nome: ", nomes[indice].capitalize())
    print("Idade: ", idades[indice])
    print("Gênero: ", generos[indice].capitalize())
    print("*-"*10)

print(f"\nA média de idade entre essas pessoas é {media} anos")
print(f"{nome_mais_velho} é a pessoa mais velha")
print(f"{nome_mais_novo} é a pessoa mais nova")
