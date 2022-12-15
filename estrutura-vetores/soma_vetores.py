'''
Faça um programa para ler dois vetores A e B, contendo N elementos cada.
Em seguida, gere um terceiro vetor C onde cada elemento de C é a soma dos
elementos correspondentes de A e B. Imprima o vetor C gerado.
'''

N: int
N = int(input("Quantos valores vai ter cada vetor? "))

A: [int] = [0 for x in range(N)]
B: [int] = [0 for x in range(N)]
C: [int] = [0 for x in range(N)]

print("Digite os valores do vetor A:")
for i in range(N):
    A[i] = int(input())

print("Digite os valores do vetor B:")
for i in range(N):
    B[i] = int(input())

for i in range(N):
    C[i] = A[i] + B[i]

print("VETOR RESULTANTE:")

for i in range(N):
    print(C[i])
