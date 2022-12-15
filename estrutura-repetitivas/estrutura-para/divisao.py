'''
Escreva um algoritmo que leia dois números e imprima o
resultado da divisão do primeiro pelo segundo. Caso não
for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.
'''

ncasos: int; numerador: int; denominador: int
divisao: float;

ncasos = int(input("Quantos casos voce vai digitar? "))

for i in range(ncasos):
	numerador = int(input("Entre com o numerador: "))
	denominador = int(input("Entre com o denominador: "))

	if denominador == 0:
		print("DIVISAO IMPOSSIVEL")
	else:
		divisao = numerador / denominador
		print(f"DIVISAO = {divisao:.2f}")