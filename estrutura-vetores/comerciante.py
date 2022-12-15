'''
Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa.
Para isto, mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de
compra e preço de venda das mesmas. Fazer um programa que leia tais dados e determine e
escreva quantas mercadorias proporcionaram:
-> lucro < 10%
-> 10% ≤ lucro ≤ 20%
-> lucro > 20%
Determine e escreva também o valor total de compra e de venda de todas as mercadorias,
assim como o lucro total.
'''

N: int; abaixo: int; entre: int; acima: int
total_compra: float; total_venda: float; lucro_total: float

N = int(input("Serao digitados dados de quantos produtos? "))

nomes: [str] = [0 for x in range(N)]
preco_compras: [float] = [0 for x in range(N)]
preco_vendas: [float] = [0 for x in range(N)]
porcentagem_lucros: [float] = [0 for x in range(N)]

for i in range(N):
    print(f"Produto {i+1}:")
    nomes[i] = str(input("Nome: "))
    preco_compras[i] = float(input("Preco de compras: "))
    preco_vendas[i] = float(input("Preco de vendas: "))

print()

for i in range(N):
    porcentagem_lucros[i] = (preco_vendas[i] - preco_compras[i]) / preco_compras[i] * 100.0

abaixo = 0
entre = 0
acima = 0

for i in range(N):
	if porcentagem_lucros[i] < 10.0:
		abaixo = abaixo + 1
	elif porcentagem_lucros[i] < 20.0:
		entre = entre + 1
	else:
		acima = acima + 1

total_compra = 0
total_venda = 0

for i in range(N):
    total_compra = total_compra + preco_compras[i]
    total_venda = total_venda + preco_vendas[i]

lucro_total = total_venda - total_compra

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
