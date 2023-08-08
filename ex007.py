import statistics

nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))

media = statistics.mean([nota1, nota2])

print(f"A média entre as notas {nota1 :.1f} e {nota2 :.1f} é {media :.1f}")