'''
Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades.
Os nomes devem ser armazenados em um vetor, e as idades em um outro vetor. Depois,
mostrar na tela o nome da pessoa mais velha.
'''

N: int; mais_velho: int; pos_mais_velho: int
N = int(input("Quantas pessoas voce vai digitar? "))

nomes: [str] = [0 for x in range(N)]
idades: [int] = [0 for x in range(N)]

for i in range(N):
    print(f"Dados da {i+1}a pessoa:")
    nomes[i] = str(input("Nome: "))
    idades[i] = int(input("Idade: "))

mais_velho = idades[0]
pos_mais_velho = 0

for i in range(N):
    if idades[i] > mais_velho:
        mais_velho = idades[i]
        pos_mais_velho = i

print(f"PESSOA MAIS VELHA: {nomes[i]}")




