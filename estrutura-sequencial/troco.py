'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.
'''

preco_unit: float; dinheiro_rec: float; troco: float
qtd: int

preco_unit = float(input("Preco unitario do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro_rec = float(input("Dinheiro recebido: "))

troco = dinheiro_rec - (qtd * preco_unit)

print(f"TROCO = {troco:.2f}")
