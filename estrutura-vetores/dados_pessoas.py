'''
Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas.
Fazer um programa que calcule e escreva a maior e a menor altura do grupo, a
média de altura das mulheres, e o número de homens.
'''

N: int; qtd_homens: int; qtd_mulheres: int
menor_altura: float; maior_altura: float; media_altura_mulheres: float; total_altura_mulheres: float

N = int(input("Quantas pessoas serao digitadas? "))

generos: [str] = [0 for x in range(N)]
alturas: [float] = [0 for x in range(N)]

for i in range(N):
    alturas[i] = float(input(f"Altura da {i+1}a pessoa: "))
    generos[i] = str(input(f"Genero da {i+1}a pessoa: "))

menor_altura = alturas[0]
maior_altura = alturas[0]

for i in range(N):
    if alturas[i] > maior_altura:
        maior_altura = alturas[i]
    if alturas[i] < menor_altura:
        menor_altura = alturas[i]

qtd_homens = 0
qtd_mulheres = 0
total_altura_mulheres = 0

for i in range(N):
    if generos[i] == 'M':
        qtd_homens = qtd_homens + 1
    else:
        qtd_mulheres = qtd_mulheres + 1
        total_altura_mulheres = total_altura_mulheres + alturas[i]

media_altura_mulheres = total_altura_mulheres / qtd_mulheres

print(f"Menor altura = {menor_altura:.2f}")
print(f"Maior altura = {maior_altura:.2f}")
print(f"Media das alturas das mulheres = {media_altura_mulheres:.2f}")
print(f"Numero de homens = {qtd_homens}")





