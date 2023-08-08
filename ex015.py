dias = int(input("Quantos dias alugados? "))
km = int(input("Quantos Km rodados? "))
pagar = dias*60 + 0.15*km

print(f"O total a pagar é de R${pagar}")