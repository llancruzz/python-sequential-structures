'''
Fazer um programa para ler dois números inteiros M e N (máximo = 10).
Em seguida, ler uma matriz de M linhas e N colunas contendo números reais.
Gerar um vetor de modo que cada elemento do vetor seja a soma dos elementos
da linha correspondente da matriz. Mostrar o vetor gerado.
'''

M: int; N: int
soma_linha: float
M = int(input("Qual a quantidade de linhas da matriz? "))
N = int(input("Qual a quantidade de colunas da matriz? "))

matriz: [[float]] = [[0 for x in range(N)] for x in range(M)]
vetor: [float] = [0 for x in range(M)]

for i in range(M):
    print(f"Digite os elementos da {i + 1}a. linha: ")
    for j in range(N):
        matriz[i][j] = float(input())

for i in range(M):
    soma_linha = 0
    for j in range(N):
        soma_linha = soma_linha + matriz[i][j]
        vetor[i] = soma_linha

print("VETOR GERADO:")

for i in range(M):
	print(f"{vetor[i]:.1f}")

