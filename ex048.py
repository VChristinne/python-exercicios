soma = 0
for num in range(1, 500):
    if (num % 2) == 1 and (num % 3) == 0:
        soma += num
print(f"A soma dos ímpares múltiplos de três é: {soma}")
