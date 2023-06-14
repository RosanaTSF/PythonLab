alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    if nome == "fim":
        break
    alunos.append(nome)

alunos_ordenados = sorted(alunos)

print("Alunos em ordem alfabética:")
for aluno in alunos_ordenados:
    print(aluno)

quantidade_alunos = len(alunos)
print("A quantidade de alunos é:", quantidade_alunos)



