'''
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma casa decimal,
bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida, o programa deve mostrar o
valor da área do terreno, bem como o valor do preço do terreno, ambos com duas casas decimais.
'''

largura: float; comprimento: float; metro_quadrado: float; area_terreno: float; preco_terreno: float

largura = float(input("Digite a largura do comprimento: "))
comprimento = float(input("Digite o comprimento do terreno: "))
metro_quadrado = float(input("Digite o valor do metro quadrado: "))

area_terreno = largura * comprimento
preco_terreno = metro_quadrado * area_terreno

print(f"Area do terreno = {area_terreno:.2f}")
print(f"Preco do terreno = {preco_terreno:.2f}")

