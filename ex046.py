import time
from colorama import Fore

print("Contagem regressiva fogos de artifício")
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(Fore.CYAN + "***** fogos de artifício *****")
