from unidecode import unidecode

frase = str(input("Digite uma frase: ")).lower().strip()
formatado = unidecode(frase)
print("A letra A aparece", formatado.count('a'), "vezes na frase")
print("A primeira letra A aparece na posição", formatado.find('a')+1)
print("A última letra A aparece na posição", formatado.rfind('a')+1)
