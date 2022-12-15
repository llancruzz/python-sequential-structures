'''
Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz
quadrada de ordem N contendo números inteiros. Em seguida, mostrar a diagonal
principal e a quantidade de valores negativos da matriz.
'''

N: int; qtd_negativos: int

N = int(input("Qual a ordem da matriz? "))

matriz: [[int]] = [[0 for x in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL:")

for i in range(N):
    print(f"{matriz[i][i]} ", end="")

qtd_negativos = 0
for i in range(N):
    for j in range(N):
        if matriz[i][j] < 0:
            qtd_negativos = qtd_negativos + 1

print(f"\nQUANTIDADE DE NEGATIVOS = {qtd_negativos}")




