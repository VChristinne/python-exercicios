from colorama import Fore

print(Fore.MAGENTA + "*** Aprovando empréstimo" + Fore.RESET)

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Anos de financiamento: "))

minimo = salario * 30 / 100
prestacao = casa / (anos * 12)

print(Fore.BLUE + f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de {prestacao:.2f}")

if prestacao <= minimo:
    print("Empréstimo concedido!")
else:
    print(Fore.RED + "Empréstimo negado!")
