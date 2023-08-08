from colorama import Fore
from datetime import datetime, date

print(Fore.RED + "*** Alistamento Militar ***" + Fore.RESET)
data_str = str(input("Data de nascimento: "))

data_format = datetime.strptime(data_str, "%d/%m/%Y")  # data formatada com horas
hoje = date.today()  # dia atual
idade = hoje.year - data_format.year - ((hoje.month, hoje.day) < (data_format.month, data_format.day))  # calcula idade
prazo = abs(idade - 18)

print(f"Sua idade é: {idade} anos")

if idade <= 0:
    print(Fore.RED + "O ano informado é maior que o ano atual!")
elif idade == 18 or idade == 17 and data_format.month <= 6:  # deve se alistar nos seis primeiros meses (janeiro a junho) do ano em que completar dezoito anos
    print(Fore.RED + "Você deve se alistar imediatamente!")
elif idade <= 16 or idade == 17 and data_format.month > 6:
    print(Fore.CYAN + f"Você não precisa se alistar! Mas falta {prazo} anos." + Fore.RESET)
elif idade >= 18:
    print(Fore.RED + f"Já passou {prazo} anos do prazo do alistamento!")
