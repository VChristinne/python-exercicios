from colorama import Style, Fore

velo_carro = int(input("Qual é a velocidade atual do carro? "))

velo_limite = 80
multa = (velo_carro-velo_limite)*7

if velo_carro > velo_limite:
    print(Fore.RED + "MULTADO! Excedeu o limite de velocidade de 80km/h\n" +
          "Irá pagar uma multa de " + Style.BRIGHT + f"R${multa:.2f}!\n" +
          Fore.GREEN + "Dirija com cuidado!")
elif velo_carro <= velo_limite:
    print(Fore.GREEN + "Dirija com cuidado")
