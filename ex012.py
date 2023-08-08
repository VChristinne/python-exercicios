preco = float(input("Qual é o preço do produto? R$"))
desconto = float(input("Qual é o valor do desconto? "))
novo_preco = preco - (preco*desconto/100)

print(f"O produto que custava R${preco:.2f}, na promoção com desconto de {desconto:.1f}% vai custar R${novo_preco:.2f}")