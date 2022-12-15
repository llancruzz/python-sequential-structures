'''
Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros,
conforme exemplo. Em seguida, mostrar na tela somente os números negativos da matriz.
'''

M: int; N: int;

M = int(input("Qual a quantidade de linhas da matriz? "))
N = int(input("Qual a quantidade de colunas da matriz? "))

matriz: [[int]] = [[0 for x in range(N)] for x in range(M)]

for i in range(M):
    for j in range(N):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("VALORES NEGATIVOS:")

for i in range(M):
    for j in range(N):
        if matriz[i][j] < 0:
            print(matriz[i][j])


