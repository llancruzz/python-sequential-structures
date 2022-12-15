'''
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora,
e a quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do
funcionário com uma mensagem explicativa.
'''

nome: str
valor_hora: float; pagamento: float
hora_trabalhada: int

nome = str(input("Nome: "))
valor_hora = float(input("Valor por hora: "))
hora_trabalhada = int(input("Horas trabalhadas: "))

pagamento = valor_hora * hora_trabalhada

print(f"O pagamento para {nome} deve ser {pagamento:.2f}")





