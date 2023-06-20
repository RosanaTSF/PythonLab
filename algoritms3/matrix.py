A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

for linha in C:
    for elemento in linha:
        print(elemento, end=" ")
    print()

A = [[1, 2, 3],
     [4, 5, 6],
     [0, 0, 0]]

for i in range(2):   
    for j in range(3): 
        A[2][j] = A[2][j] + A[i][j]

for linha in A:
    for elemento in linha:
        print(elemento, end=" ")
    print()