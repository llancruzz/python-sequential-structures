'''
Uma empresa vai conceder um aumento percentual de salário aos seus
funcionários dependendo de quanto 20% cada pessoa ganha, conforme
tabela abaixo. Fazer um 15% programa para ler o salário de uma pessoa,
daí mostrar qual o novo salário desta pessoa depois do aumento,
quanto foi o aumento e qual foi a porcentagem de aumento.

Salario atual:
Ate R$ 1000,00 - aumemento de 20%
Acima de R$ 1000.00 ate R$ 3000.000 - aumento de 15%
Acima de R$ 3000.00 ate R$ 8000.000 - aumento de 10
Acima de R$ 8000.00 - aumento de 5%
'''

salario: float; novo_salario: float; aumento: float; porcentagem: float

salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000:
    porcentagem = 20
elif salario <= 3000:
    porcentagem = 15
elif salario <= 8000:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario * porcentagem / 100
novo_salario = salario + aumento

print(f"Novo salario = R${novo_salario:.2f}")
print(f"Aumento = R${aumento:.2f}")
print(f"Porcentagem = {porcentagem}%")

'''
salario: float; novosalario: float; aumento: float
porcentagem: int

salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000.0:
	porcentagem = 20
	aumento = salario * porcentagem / 100
	novosalario = salario + aumento
elif salario <= 3000.0:
	porcentagem = 15
	aumento = salario * porcentagem / 100
	novosalario = salario + aumento
elif salario <= 8000.0:
	porcentagem = 10
	aumento = salario * porcentagem / 100
	novosalario = salario + aumento
else:
	porcentagem = 5
	aumento = salario * porcentagem / 100
	novosalario = salario + aumento

print(f"Novo salario = R$ {novosalario:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {porcentagem} %")
'''

