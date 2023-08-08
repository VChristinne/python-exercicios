from colorama import Fore

print(Fore.GREEN + "*** Conversão de bases numéricas ***" + Fore.RESET)
num = int(input("Digite um número para a conversão: "))
print("(1) - Binário\n" + "(2) - Octal\n" + "(3) - Hexadecimal")
opc = int(input("Insira uma opção: "))

if opc == 1:
    print(Fore.GREEN + f"O número {num} em binário é: {bin(num)}")
elif opc == 2:
    print(Fore.GREEN + f"O número {num} em octal é: {oct(num)}")
elif opc == 3:
    print(Fore.GREEN + f"O número {num} em hexadecimal é: {hex(num)}")
else:
    print(Fore.RED + "Opção inválida! Tente novamente.")
