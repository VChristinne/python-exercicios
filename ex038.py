num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))

if num1 == num2:
    print("Não existe valor maior, os dois são iguais")
else:
    print(f"O número {max([num1, num2])} é maior")
