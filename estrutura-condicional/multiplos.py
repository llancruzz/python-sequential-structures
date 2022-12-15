'''
Fazer um programa para ler dois números inteiros, e dizer se um número
é múltiplo números podem ser digitados em qualquer ordem.
'''

numero1: int; numero2: int

print("Digite dois numeros inteiros:")
numero1 = int(input())
numero2 = int(input())

if numero1 % numero2 == 0 or numero2 % numero1 == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")
