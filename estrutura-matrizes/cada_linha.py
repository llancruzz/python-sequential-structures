'''
Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10).
Mostrar qual o maior elemento de cada linha. Suponha não haver empates.
'''

N: int; maior: int

N = int(input("Qual a ordem da matriz? "))

matriz: [[int]] = [[0 for x in range(N)] for x in range(N)]
maiorlinha: int = []

for i in range(N):
    for j in range(N):
        matriz[i][j] = int(input(f"Elemento [{i}, {j}]: "))

for i in range(N):
    maior = matriz[i][0]
    for j in range(1, N):
        if maior < matriz[i][j]:
            maior = matriz[i][j]
            
    maiorlinha.append(maior)

print("MAIOR ELEMENTO DE CADA LINHA:")

for i in range(N):
    print(maiorlinha[i])