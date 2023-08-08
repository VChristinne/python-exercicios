from random import randrange
from colorama import Fore, Style, Back

print(Fore.RED + Style.BRIGHT + "*** Tente adivinhar o número ***\n" + Style.RESET_ALL,
      Fore.BLUE + "\nEscolha uma dificuldade: " + Style.RESET_ALL,
      Fore.CYAN + "\n(1) - Fácil \nRegras: número entre 0 e 5 com 3 tentativas.\n",
      "\n(2) - Médio \nRegras: número entre 0 e 15 com 4 tentativas.\n",
      "\n(3) - Difícil \nRegras: número entre 0 e 100 com 5 tentativas.\n" + Style.RESET_ALL)
nivel = int(input('Selecione um nível: '))

if nivel == 1:
    tentativas = 3
    num_escolhido = randrange(5)

elif nivel == 2:
    tentativas = 4
    num_escolhido = randrange(15)

elif nivel == 3:
    tentativas = 5
    num_escolhido = randrange(100)

for rodada in range(1, tentativas + 1):
    print(f"Tentativa {rodada} de {tentativas}")

    if rodada == tentativas:
        print("Esta é sua ÚLTIMA tentativa!")

    chute = int(input("Qual o seu chute? "))

    acertou = chute == num_escolhido
    maior = chute > num_escolhido
    menor = chute < num_escolhido
    perdeu = rodada == tentativas and chute != num_escolhido

    if acertou:
        print(Fore.BLUE + Style.BRIGHT + "Parabéns, você acertou!")
        break

    elif maior:
        print(Fore.MAGENTA + "Seu chute foi maior que o número pensado pelo computador\n" + Style.RESET_ALL)
        if perdeu: print(Fore.RED + Style.BRIGHT + f"Você perdeu! O número pensado foi {num_escolhido}")

    elif menor:
        print(Fore.MAGENTA + "Seu chute foi menor que o número pensado pelo computador\n" + Style.RESET_ALL)
        if perdeu: print(Fore.RED + Style.BRIGHT + f"Você perdeu! O número pensado foi {num_escolhido}")
