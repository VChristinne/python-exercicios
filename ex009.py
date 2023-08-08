print("*** TABUADA ***")
num = int(input("Digite um número: "))

print("------------")
for num_ordem in range(11):
    print(f"{num} x {num_ordem} = {num*num_ordem}")
print("------------")
