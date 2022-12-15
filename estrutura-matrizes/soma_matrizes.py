'''
Fazer um programa para ler duas matrizes de números inteiros A e B,
contendo de M linhas e N colunas cada (M e N máximo = 10). Depois,
gerar uma terceira matriz C onde cada elemento desta é a soma dos
elementos correspondentes das matrizes originais. Imprimir na tela
a matriz gerada.
'''

M: int; N: int;

M = int(input("Quantas linhas vai ter cada matriz? "))
N = int(input("Quantas colunas vai ter cada matriz? "))

A: [[int]] = [[0 for x in range(N)] for x in range(M)]
B: [[int]] = [[0 for x in range(N)] for x in range(M)]
C: [[int]] = [[0 for x in range(N)] for x in range(M)]

print("Digite os valores da matriz A:")
for i in range(M):
    for j in range(N):
        A[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Digite os valores da matriz B:")
for i in range(M):
    for j in range(N):
        B[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(M):
    for j in range(N):
        C[i][j] = A[i][j] + B[i][j]

print("MATRIZ SOMA:")

for i in range(M):
	for j in range(N):
		print(f"{C[i][j]} ", end="")
	print()

