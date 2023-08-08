import numpy as np
from colorama import Fore

print(Fore.MAGENTA + "*** Média das notas ***" + Fore.RESET)

notas = []
for i in range(2):
    notas.append(float(input("Nota do aluno: ")))

media = np.mean(notas)

if media < 5.0:
    print(Fore.RED + "Reprovado!".upper())
elif 5 < media < 6.9:
    print(Fore.YELLOW + "Recuperação!".upper())
else:
    print(Fore.GREEN + "Aprovado!".upper())
