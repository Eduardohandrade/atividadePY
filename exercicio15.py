#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída:
#Ex: Tibúrcio, você já viveu 6935 dias.
#Lê o nome e a idade da pessoa
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Calcula a quantidade de dias de vida
dias_de_vida = idade * 365

# Exibe a quantidade de dias de vida da pessoa
print(nome + ", você já viveu " + str(dias_de_vida) + " dias.")