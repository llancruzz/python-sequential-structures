'''
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo
semestres de uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve
(com uma casa decimal) no ano juntamente com um texto explicativo. Caso a nota final
do aluno seja inferior a 60.00, mostrar a mensagem "REPROVADO".
'''

nota1: float; nota2: float; nota_final: float

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

nota_final = nota1 + nota2

print(f"NOTA FINAL = {nota_final:.1f}")

if nota_final < 60.0:
	print("REPROVADO")
