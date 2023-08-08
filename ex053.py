print("*** Palíndromo ***\n")
frase = str(input("Digite uma frase ou palavra: ")).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

if inverso == junto:
    print("Palíndromo")
else:
    print("Não é um palíndromo")
