from datetime import datetime, date
from colorama import Fore

print(Fore.CYAN + "*** Categoria dos nadadores ***" + Fore.RESET)
data_str = str(input("Data de nascimento: "))

data_format = datetime.strptime(data_str, "%d/%m/%Y")  # data formatada com horas
hoje = date.today()  # dia atual
idade = hoje.year - data_format.year - ((hoje.month, hoje.day) < (data_format.month, data_format.day))  # calcula idade

if idade <= 0:
    print(Fore.RED + "O ano informado é maior que o ano atual!")
elif idade <= 9:
    print(Fore.BLUE + f"Jovens de {idade} anos estão na categoria Mirim")
elif idade <= 14:
    print(Fore.BLUE + f"Jovens de {idade} anos estão na categoria Infantil")
elif idade <= 19:
    print(Fore.BLUE + f"Jovens de {idade} anos estão na categoria Junior")
elif idade <= 25:
    print(Fore.BLUE + f"Adultos de {idade} anos estão na categoria Sênior")
else:
    print(Fore.BLUE + f"Adultos de {idade} anos estão na categoria Master")
