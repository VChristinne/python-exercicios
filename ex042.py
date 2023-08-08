from colorama import Fore

# condição da existência de um triângulo: soma das medidas de dois deles é sempre maior que a medida do terceiro
# equilátero: lados iguais, isósceles: dois lados iguais, escaleno: todos diferentes
print(Fore.BLUE + "-=-=-=- Condição da existência de um triângulo -=-=-=-" + Fore.RESET)

lad1 = int(input("Insira um lado do triângulo: "))
lad2 = int(input("Insira um lado do triângulo: "))
lad3 = int(input("Insira um lado do triângulo: "))

ordem = sorted([lad1, lad2, lad3])

if ordem[0] + ordem[1] >= ordem[2]:
    print(Fore.GREEN + "O triângulo pode ser formado")
    if ordem[0] == ordem[1] == ordem[2]:
        print("Será formado um triângulo equilátero")
    elif ordem[0] == ordem[1] or ordem[0] == ordem[2] or ordem[1] == ordem[2]:
        print("Será formado um triângulo isósceles")
    elif ordem[0] != ordem[1] != ordem[2]:
        print("Será formado um triângulo escaleno")
elif ordem[1] < ordem[2]:
    print(Fore.MAGENTA + "O triângulo não pode ser formado")
