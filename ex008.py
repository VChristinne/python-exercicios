medida = float(input("Uma distância em metros: "))

km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000

print(f"A medida de {medida} corresponde a: ")
print(f"{km} quilômetros")
print(f"{hm} hectômetros")
print(f"{dam} decâmetros")
print(f"{dm} decímetros")
print(f"{cm} centímetros")
print(f"{mm} milímetros")