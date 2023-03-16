def primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    return i == num


for n in range(2, 100):
    if not primo(n):
        continue
print(n)


ListaAlunos = ['Plínio',7,9,'Pedro',5,9] 
for aluno in ListaAlunos:
    pass
print('the-end')
