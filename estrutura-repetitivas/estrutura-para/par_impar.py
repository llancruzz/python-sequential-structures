'''
Leia um valor inteiro N. Este valor será a quantidade de números inteiros
que serão lidos em seguida. Para cada valor lido, mostre uma mensagem
dizendo se este valor lido é PAR ou IMPAR, e também se é POSITIVO ou
NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá
imprimir apenas NULO.
'''

n: int; valor: int

n = int(input("Quantos numeros voce vai digitar? "))

for i in range(n):
	valor = int(input("Digite um numero: "))

	if valor == 0:
		print("NULO")
	else:
		if valor % 2 == 0:
			print("PAR", end="")
		else:
			print("IMPAR", end="")
		if valor > 0:
			print(" POSITIVO")
		else:
			print(" NEGATIVO")
