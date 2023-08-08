from random import choice

alunos = []

for i in range(4):
    alunos.append(input("Nome do aluno: "))

print(f"O aluno escolhido foi {choice(alunos)}")
