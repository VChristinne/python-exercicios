soma = 0
for c in range(1, 7):
    valor = int(input(f"Digite o {c} valor: "))

    if (valor % 2) == 0:
        soma += valor

print(f"A soma dos números pares é: {soma}")
