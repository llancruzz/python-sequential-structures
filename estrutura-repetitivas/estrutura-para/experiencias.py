'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina
e precisa de sua ajuda para organizar os experimentos de um laboratório
o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias
foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos.
Para obter estas informações, ela sabe exatamente o número de experimentos que foram
realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada
experimento. Faça um programa que leia um valor inteiro N que indica os vários casos
de teste que vem a seguir. Cada caso de teste contém um inteiro que representa a
quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o
total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao
total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois
dígitos após o ponto.
'''

N: int; qtd_cobaias: int; total_cobaias: int; total_coelhos: int; total_ratos: int; total_sapos: int
perc_coelhos: float; perc_ratos: float; perc_sapos: float
tipo_cobaia: str

N = int(input("Quantos casos de testes serao digitados? "))

total_sapos = 0
total_coelhos = 0
total_ratos = 0

for i in range(N):
    qtd_cobaias = int(input("Quantidade de cobaias: "))
    tipo_cobaia = str(input("Tipo de cobaia: "))

    if tipo_cobaia == "C":
        total_coelhos = total_coelhos + qtd_cobaias
    elif tipo_cobaia == "R":
        total_ratos = total_ratos + qtd_cobaias
    else:
        total_sapos = total_sapos + qtd_cobaias

total_cobaias = total_sapos + total_coelhos + total_ratos
perc_coelhos = total_coelhos / total_cobaias * 100
perc_ratos = total_ratos / total_cobaias * 100
perc_sapos = total_sapos / total_cobaias * 100

print()
print("RELATORIO FINAL")
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f}")
print(f"Percentual de ratos: {perc_ratos:.2f}")
print(f"Percentual de sapos: {perc_sapos:.2f}")




















