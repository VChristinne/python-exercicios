from colorama import Fore
num = int(input("Digite um número: "))
print(Fore.BLUE + "Essa número é par") if num % 2 == 0 else print(Fore.GREEN + "Esse número é ímpar")
