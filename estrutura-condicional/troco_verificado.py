'''
Fazer um programa para calcular o troco no processo de pagamento de um
produto de uma mercearia. O programa deve ler o preço unitário do
produto, a quantidade de unidades compradas deste produto, e o valor
em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do
troco a ser devolvido ao cliente. Se o dinheiro dado pelo cliente não
for suficiente, mostrar uma mensagem informando o valor restante.
'''

preco: float; dinheiro: float; troco: float; faltam: float
qtd: int

preco = float(input("Preco unitario do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

if preco * qtd > dinheiro:
	faltam = preco * qtd - dinheiro
	print(f"DINHEIRO INSUFICIENTE. FALTAM {faltam:.2f} REAIS")
else:
	troco = dinheiro - preco * qtd
	print(f"TROCO = {troco:.2f}")




