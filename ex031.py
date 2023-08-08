dist = float(input("Qual é a distância de uma viagem em Km? "))
preco = 0.50 * dist if dist <= 200 else dist * 0.45
print(f"O preço equivalente a sua viagem de {dist}Km será de R${preco:.2f}")
