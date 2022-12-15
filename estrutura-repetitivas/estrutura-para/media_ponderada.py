'''
Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir.
Cada caso de teste consiste de 3 valores reais, para os quais você deverá calcular
e mostrar a média ponderada, sendo que o primeiro valor tem peso 2, o segundo valor
tem peso 3 e o terceiro valor tem peso 5. Vale lembrar que a média ponderada é a
soma de todos os valores multiplicados pelo seu respectivo peso, dividida pela
soma dos pesos.
'''

N: int
A: float; B: float; C: float; media: float

N = int(input("Quantos casos voce vai digitar? "))

for i in range(N):
    print("Digite tres numeros:")
    A = float(input())
    B = float(input())
    C = float(input())
    media = (A * 2 + B * 3 + C * 5) / 10
    print(f"MEDIA = {media:.1f}")



