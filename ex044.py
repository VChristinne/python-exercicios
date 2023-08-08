from colorama import Fore

titulo = (Fore.BLUE + "=" * 20 + " Lojas Chris " + "=" * 20 + Fore.RESET)
print(titulo.center(50))

preco = float(input("Preço das compras: R$"))

print("\n* Formas de pagamento *\n" +
      "(1) à vista dinheiro/cheque\n" +
      "(2) à vista cartão\n" +
      "(3) 2x no cartão\n" +
      "(4) 3x ou mais no cartão\n")
opc = int(input("Digite a opção: "))

if opc == 1:
    total = preco - (preco * 10 / 100)
elif opc == 2:
    total = preco - (preco * 5 / 100)
elif opc == 3:
    total = preco
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f}")
elif opc == 4:
    total = preco + (preco * 20 / 100)
    quant_parcelas = int(input("Quantidade de parcelas: "))
    parcela = total/quant_parcelas
    print(f"Sua compra será parcelada em {quant_parcelas}x de R${parcela:.2f} com juros")
else:
    print(Fore.RED + "Opção inválida!")
print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final")
