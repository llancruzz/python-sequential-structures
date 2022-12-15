import math

'''
Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais.
Em seguida, fazer as seguintes ações:
a) calcular e imprimir a soma de todos os elementos positivos da matriz.
b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir
todos os elementos desta linha.
c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir
todos os elementos desta coluna. d) imprimir os elementos da diagonal
principal da matriz.
e) alterar a matriz elevando ao quadrado todos os números negativos da mesma.
Em seguida imprimir a matriz alterada.
'''

n: int; indlinha: int; indcoluna: int
somapositivos: float

n = int(input("Qual a ordem da matriz? "))

matriz: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
	for j in range(n):
		matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))

somapositivos = 0
for i in range(n):
	for j in range(n):
		if matriz[i][j] > 0:
			somapositivos = somapositivos + matriz[i][j]

print(f"\nSOMA DOS POSITIVOS: {somapositivos:.1f}\n")

indlinha = int(input("Escolha uma linha: "))

print("LINHA ESCOLHIDA: ", end="");

for i in range(n):
	print(f"{matriz[indlinha][i]:.1f} ", end="")

indcoluna = int(input("\n\nEscolha uma coluna: "))

print("COLUNA ESCOLHIDA: ", end="");

for i in range(n):
	print(f"{matriz[i][indcoluna]:.1f} ", end="")

print("\n\nDIAGONAL PRINCIPAL: ", end="");

for i in range(n):
	print(f"{matriz[i][i]:.1f} ", end="")

for i in range(n):
	for j in range(n):
		if matriz[i][j] < 0:
			matriz[i][j] = math.pow(matriz[i][j], 2);

print("\n\nMATRIZ ALTERADA:");

for i in range(n):
	for j in range(n):
		print(f"{matriz[i][j]:.1f} ", end="")
	print()
