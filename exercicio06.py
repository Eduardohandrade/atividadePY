#Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre.
#No final informar o nome do aluno e a sua média (aritmética) em python.
ome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

print("O aluno", "obteve a média aritmética", media)