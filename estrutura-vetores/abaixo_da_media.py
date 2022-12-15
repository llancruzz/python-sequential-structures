'''
Fazer um programa para ler um número inteiro N e depois um vetor de N números reais.
Em seguida, mostrar na tela a média aritmética de todos elementos com três casas decimais.
Depois mostrar todos os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.
'''

N: int;
media_vetor: float; soma_vetor: float
N = int(input("Quantos elementos vai ter o vetor? "))

vetor: [float] = [0 for x in range(N)]

for i in range(N):
    vetor[i] = float(input("Digite um numero: "))

soma_vetor = 0
for i in range(N):
    soma_vetor = soma_vetor + vetor[i]

media_vetor = soma_vetor / N

print()
print(f"MEDIA DO VETOR = {media_vetor:.3f}")

print("ELEMENTOS ABAIXO DA MEDIA:")

for i in range(N):
    if vetor[i] < media_vetor:
        print(vetor[i])




