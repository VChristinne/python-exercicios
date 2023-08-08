print("*** Conversor de moedas ***")
real = float(input("Quanto deseja converter? R$"))

dolar = real/5.25
euro = real/6.20
won = real/0.0045
iene = real/0.048
libra = real/7.28

print(f"R${real} dá: ")
print(f"{dolar :.2f} dólares")
print(f"{euro :.2f} euros")
print(f"{won :.2f} won")
print(f"{iene :.2f} ienes japônes")
print(f"{libra :.2f} libras esterlina")