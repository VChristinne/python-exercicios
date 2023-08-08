from unidecode import unidecode

nome = str(input("Qual o seu nome completo? ")).lower().strip()
formatado = unidecode(nome).split()
print(f"Seu primeiro nome é {formatado[0]}")
print(f"Seu último nome é {formatado[len(formatado)-1]}")
