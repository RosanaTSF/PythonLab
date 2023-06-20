import random

ordem = int(input("Informe a ordem da matriz quadrada: "))

if ordem > 0:
    matriz = []

    for _ in range(ordem):
        linha = [random.randint(1, 10) for _ in range(ordem)]
        matriz.append(linha)

    print("Matriz Quadrada:")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()

    diagonal_principal = [matriz[i][i] for i in range(ordem)]
    maior_diagonal_principal = max(diagonal_principal)

    diagonal_secundaria = [matriz[i][ordem - 1 - i] for i in range(ordem)]
    menor_diagonal_secundaria = min(diagonal_secundaria)

    media = (maior_diagonal_principal + menor_diagonal_secundaria) / 2

    print("Maior valor da diagonal principal:", maior_diagonal_principal)
    print("Menor valor da diagonal secundária:", menor_diagonal_secundaria)
    print("Média entre os dois valores:", media)

else:
    print("A ordem da matriz deve ser maior que zero.")
