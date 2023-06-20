import random

while True:
    linhas = int(input("Informe o número de linhas: "))
    colunas = int(input("Informe o número de colunas: "))

    if linhas > 0 and colunas > 0:
        matriz = []

        for _ in range(linhas):
            linha = [random.randint(13, 23) for _ in range(colunas)]
            matriz.append(linha)

        for linha in matriz:
            for elemento in linha:
                print(elemento, end=" ")
            print()

        break
    else:
        print("O número de linhas e colunas deve ser maior que zero.")