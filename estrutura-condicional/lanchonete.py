'''
Uma lanchonete possui vários produtos. Cada produto possui um código e um preço.
Você deve fazer um programa para ler o código e a quantidade comprada de um produto
(suponha um código válido), e daí informar qual o valor a ser pago, com duas casas
decimais, conforme tabela de produtos abaixo:

Codigo e precos dos produtos:
1 = R$ 5.00
2 = R$ 3.50
3 = R$ 4.80
4 = R$ 8.90
5 = R$ 7.32

'''

codigo: int; qtd_comprada: int
valor_pagar: float

codigo = int(input("Codigo do produto comprado: "))
qtd_comprada = int(input("Quantidade comprada: "))

valor_pagar = 0
if codigo == 1:
    valor_pagar = qtd_comprada * 5.0
elif codigo == 2:
    valor_pagar = qtd_comprada * 3.5
elif codigo == 3:
    valor_pagar = qtd_comprada * 4.8
elif codigo == 4:
    valor_pagar = qtd_comprada * 8.90
elif codigo == 5:
    valor_pagar = qtd_comprada * 7.32

print(f"Valor a pagar: R${valor_pagar:.2f}")
