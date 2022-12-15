'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade
indeterminada de pontos no sistema cartesiano. Para cada ponto escrever
o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O algoritmo será
encerrado quando pelo menos uma de duas coordenadas for
NULA (nesta situação sem escrever mensagem alguma).
'''

x: int; y: int

print("Digite os valores das coordenadas X e Y:")

x = int(input())
y = int(input())

while x  != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE 1")
    elif x < 0 and y > 0:
        print("QUADRANTE 2")
    elif x < 0 and y < 0:
        print("QUADRANTE 3")
    else:
        print("QUADRANTE 4")

    print("Digite os valores das coordenadas X e Y:")
    x = int(input())
    y = int(input())

