print("*** Progressão Aritmética ***\n")

t1 = int(input(f"Primeiro termo da P.A: "))
razao = int(input(f"Razão da P.A: "))
decimo = t1 + (10 - 1) * razao

for pa in range(t1, decimo + razao, razao):
    print(f"{pa}", end=" -> ")
print(f"FIM")
