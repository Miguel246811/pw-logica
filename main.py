aluno1 = "Apollo"
aluno2 = "Miguel"
aluno3 = "Bernardo"

alunos = ["Pedro", "Miguel", "Apollo", "Bernardo"]
print(alunos)
alunos.remove("João")
alunos.pop(2)
print(alunos)

quantidade = len(alunos)
print(f"Temos {quantidade} alunos cadatrados. ")

for aluno in alunos:
    print(f"Olá, {aluno}!")
for contador in range(4):
    print(alunos[contador])
