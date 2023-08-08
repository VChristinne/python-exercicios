salario = float(input("Qual é o salário do funcionário? R$"))
aumento = float(input("Qual é a percentagem de aumento? "))
novo_salario = salario + (salario*aumento/100)

print(f"Um funcionário que ganhava R${salario:.2f}, com {aumento:.2f}% de aumento, passará a ganhar R${novo_salario:.2f}")