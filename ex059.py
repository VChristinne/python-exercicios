# CALCULADORA
from colorama import Fore, Style

print(Fore.RED + Style.BRIGHT + "*** CALCULADORA ***\n" + Style.RESET_ALL,
      Fore.BLUE + "\n(1) - SOMAR \n",
      "\n(2) - SUBTRAÇÃO \n",
      "\n(3) - MULTIPLICAÇÃO \n",
      "\n(4) - DIVISÃO \n" + Style.RESET_ALL)
opc = int(input('Selecione uma opção: '))
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

if opc == 1: result = n1 + n2
elif opc == 2: result = n1 - n2
elif opc == 3: result = n1 * n2
elif opc == 4: result = n1 / n2
