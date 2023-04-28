#Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total 
#percorrida pelo automóvel e o total de combustível gasto
distancia = float(input("Digite a distância percorrida pelo automóvel (em km): "))
combustivel = float(input("Digite o total de combustível gasto pelo automóvel (em litros): "))

consumo_medio = distancia / combustivel

print("O consumo médio do automóvel é de", consumo_medio, "km/l")