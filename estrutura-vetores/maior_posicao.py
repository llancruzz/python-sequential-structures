'''
Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida,
mostrar na tela o maior número do vetor (supor não haver empates). Mostrar também
a posição do maior elemento, considerando a primeira posição como 0 (zero).
'''

N: int; pos_maior: int
maior: float
N = int(input("Quantos numeros voce vai digitar? "))

vetor: [float] = [0 for x in range(N)]

for i in range(N):
    vetor[i] = float(input("Digite um numero: "))

maior = vetor[0]
pos_maior = 0
for i in range(N):
    if vetor[i] > maior:
        maior = vetor[i]
        pos_maior = i

print(f"\nMAIOR VALOR = {maior:.1f}")
print(f"POSICAO DO MAIOR VALOR = {pos_maior}")


