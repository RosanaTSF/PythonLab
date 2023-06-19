elemento = []

while True:
    nome_personagem = input("Nome do personagem: ")
    elemento.append(nome_personagem.upper())

    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() != 's':
        break

print(elemento)

print(len(elemento))
