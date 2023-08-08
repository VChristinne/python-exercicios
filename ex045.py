from colorama import Fore, Style
from random import randint

titulo = Fore.RED + Style.BRIGHT + "Jokenpô" + Style.RESET_ALL
print(Fore.YELLOW + "-=-=-" * 10)
print(titulo.center(60))
print(Fore.YELLOW + "-=-=-" * 10)

print(Fore.WHITE + "Regras: \nA tesoura(3) ganha do papel(2), mas perde para a pedra(1); \n"
                   "O papel(2) ganha da pedra(1), mas perde para tesoura(3)\n"
                   "A pedra(1) ganha da tesoura(3), mas perde para o papel(2).\n" + Fore.RESET)

opc = int(input("Digite o número que representa a opção que deseja jogar: \n" +
                "(0) - Pedra\n" +
                "(1) - Papel\n" +
                "(2) - Tesoura\n"))

nomes = ("pedra", "papel", "tesoura")
bot = randint(0, 2)

if opc == 0 and bot == 2:
    print(Fore.BLUE + f"Você ganhou! O computador escolheu {nomes[bot]} e você escolheu {nomes[opc]}")
elif opc == 1 and bot == 0:
    print(Fore.BLUE + f"Você ganhou! O computador escolheu {nomes[bot]} e você escolheu {nomes[opc]}")
elif opc == 2 and bot == 1:
    print(Fore.BLUE + f"Você ganhou! O computador escolheu {nomes[bot]} e você escolheu {nomes[opc]}")
elif opc == bot:
    print("Empate!")
else:
    print(Fore.RED + f"Você perdeu! O computador escolheu {nomes[bot]} e você escolheu {nomes[opc]}")
