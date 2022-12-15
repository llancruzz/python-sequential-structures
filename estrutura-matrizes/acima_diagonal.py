'''
Ler um inteiro N (máximo = 10) e uma matriz quadrada de ordem N contendo números inteiros.
Mostrar a soma dos elementos acima da diagonal principal. Um exemplo de números acima da
diagonal principal é mostrado ao lado (no caso as células com fundo cinza).
'''

N: int; soma: int
N = int(input("Qual a ordem da matriz? "))

matriz: [[int]] = [[0 for x in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        matriz[i][j] = int(input(f"Elemento [{i}, {j}]: "))

soma = 0
for i in range(N):
    for j in range(N):
        if i < j:
            soma = soma + matriz[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}")
