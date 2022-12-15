'''
Fazer um programa para ler um vetor de N números inteiros.
Em seguida, mostrar na tela a média aritmética somente dos
números pares lidos, com uma casa decimal. Se nenhum número
par for digitado, mostrar a mensagem "NENHUM NUMERO PAR"
'''

N: int; soma: int; cont_pares: int
media: float
N = int(input("Quantos elementos vai ter o vetor? "))

vetor: [int] = [0 for x in range(N)]

for i in range(N):
    vetor[i] = int(input("Digite um numero: "))

soma = 0
cont_pares = 0

for i in range(N):
    if vetor[i] % 2 == 0:
        soma = soma + vetor[i]
        cont_pares = cont_pares + 1

if cont_pares == 0:
    print("NENHUM NUMERO PAR")
else:
    media = soma / cont_pares
    print(f"MEDIA DOS PARES = {media:.1f}")




