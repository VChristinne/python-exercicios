cidade = str(input("Qual o nome da sua cidade? ")).strip()
result = (cidade[:5].lower() == "santo")
if result:
    print("Essa cidade começa com a palavra Santo")
else:
    print("Essa cidade não começa com a palavra Santo")
