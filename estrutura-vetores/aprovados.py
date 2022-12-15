'''
Fazer um programa para ler um conjunto de N nomes de alunos, bem como as
notas que eles tiraram no 1o e 2o semestres. Cada uma dessas informações
deve ser armazenada em um vetor. Depois, imprimir os nomes dos alunos aprovados,
considerando aprovados aqueles cuja média das notas seja maior ou igual a 6.0 (seis).
'''

N: int
media: float
N = int(input("Quantos alunos serao digitados? "))

nomes: [str] = [0 for x in range(N)]
primeira_nota: [float] = [0 for x in range(N)]
segunda_nota: [float] = [0 for x in range(N)]

for i in range(N):
    print(f"Digite nome, primeira e segunda nota do {i+1}a aluno:")
    nomes[i] = str(input())
    primeira_nota[i] = float(input())
    segunda_nota[i] = float(input())

print("Alunos aprovados:")

for i in range(N):
    media = (primeira_nota[i] + segunda_nota[i]) / 2
    if media >= 6:
        print(nomes[i])


