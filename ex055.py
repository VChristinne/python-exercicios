pesos = []

for p in range(1, 6):
    peso = pesos.append(float(input(f"Peso da {p} pessoa: ")))

print(f"O menor peso é {min(pesos)} Kg")
print(f"O maior peso é {max(pesos)} Kg")
