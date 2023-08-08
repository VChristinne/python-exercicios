from random import shuffle

alunos = []

for i in range(4):
    alunos.append(input("Nome do aluno: "))
shuffle(alunos)

print(f"A ordem de apresentação será: {alunos}")
