from colorama import Fore

# condição da existência de um triângulo: soma das medidas de dois deles é sempre maior que a medida do terceiro
print(Fore.BLUE + "-=-=-=- Condição da existência de um triângulo -=-=-=-" + Fore.RESET)

lad1 = int(input("Insira um lado do triângulo: "))
lad2 = int(input("Insira um lado do triângulo: "))
lad3 = int(input("Insira um lado do triângulo: "))

ordem = sorted([lad1, lad2, lad3])

if ordem[0] + ordem[1] >= ordem[2]:
    print(Fore.GREEN + "O triângulo pode ser formado")
else:
    print(Fore.MAGENTA + "O triângulo não pode ser formado")
