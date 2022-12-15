'''
Faça um programa para ler um número indeterminado de dados, contendo cada um,
a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém
um valor de idade negativa. Calcular e imprimir a idade média deste grupo de
indivíduos. Se for entrado um valor negativo na primeira vez,mostrar a mensagem
"IMPOSSIVEL CALCULAR".
'''


idade: int; cont_pessoas: int
soma: float; media: float

print("Digite as idades:")
idade = int(input())

if idade < 0:
	print("IMPOSSIVEL CALCULAR")
else:
	soma = 0
	cont_pessoas = 0
	while idade >= 0:
		soma = soma + idade
		cont_pessoas = cont_pessoas + 1
		idade = int(input())

	media = soma / cont_pessoas

	print(f"MEDIA = {media:.2f}")
