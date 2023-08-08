from colorama import Fore

# cálculo IMC: peso/pow(altura, 2)
print(Fore.BLUE + "*** Cálculo do IMC ***" + Fore.RESET)
alt = float(input("Altura: "))
peso = float(input("Peso: "))
imc = peso/alt**2
print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
    print(Fore.RED + "Abaixo do peso!")
elif imc < 25:
    print(Fore.BLUE + "Peso ideal!")
elif imc < 30:
    print(Fore.YELLOW + "Sobrepeso!")
elif imc <= 40:
    print(Fore.YELLOW + "Obesidade!")
else:
    print(Fore.RED + "Obesidade mórbida!!!")
