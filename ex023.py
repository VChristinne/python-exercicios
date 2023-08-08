num = int(input("Digite um número entre 0 e 9999: "))
if 9999 > num > 0:
    n = f"{num:>4}"
    print(f"Unidade: {n[3]}",
          f"\nDezena: {n[2]}",
          f"\nCentena: {n[1]}",
          f"\nMilhar: {n[0]}")
else:
    print("Esse número é inválido. Tente um número entre 0 e 9999")
