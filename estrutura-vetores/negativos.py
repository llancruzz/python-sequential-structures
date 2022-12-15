'''
Faça um programa que leia um número inteiro positivo N (máximo = 10) e
depois N números inteiros e armazene-os em um vetor. Em seguida, mostrar
na tela todos os números negativos lidos.
'''

N: int

N = int(input("Quantos numeros voce vai digitar? "))
vetor: [int] = [0 for x in range(N)]

for i in range(N):
    vetor[i] = int(input("Digite um numero: "))

print("NUMEROS NEGATIVOS")
for i in range(N):
    if vetor[i] < 0:
        print(vetor[i])


