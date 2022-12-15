'''
Faça um programa que leia N números inteiros e armazene-os em um vetor.
Em seguida, mostre na tela todos os números pares, e também a quantidade
de números pares.
'''

n: int; qtdpares: int

n = int(input("Quantos numeros voce vai digitar? "))

vetor: [int] = [0 for x in range(n)]

for i in range(n):
	vetor[i] = int(input("Digite um numero: "))

print("\nNUMEROS PARES:")

qtdpares = 0
for i in range(n):
	if vetor[i] % 2 == 0:
		print(f"{vetor[i]}  ", end="")
		qtdpares = qtdpares + 1

print(f"\n\nQUANTIDADE DE PARES = {qtdpares}")








