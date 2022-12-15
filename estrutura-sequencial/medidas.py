
'''
Fazer um programa para ler três medidas A, B e C.
Em seguida, calcular e mostrar (imprimir os dados com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C
'''

a: float; b: float; c: float; area_quadrado: float; area_triangulo: float; area_trapezio: float

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

area_quadrado = a * a
area_triangulo = (a * b) / 2
area_trapezio = (a + b) / 2 * c

print(f"AREA DO QUADRADO = {area_quadrado:.4f}")
print(f"AREA DO TRIANGULO = {area_triangulo:.4f}")
print(f"AREA DO TRAPEZIO = {area_trapezio:.4f}")