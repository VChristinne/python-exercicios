#from typing import List

nome = str(input("Qual o seu nome completo? ")).strip()

print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome contém {len(nome)-nome.count(' ')} letras")
#dividido: List[str] = nome.split()
#print(len(dividido[0]))
print(f"Seu primeiro nome tem {nome.find(' ')} letras")