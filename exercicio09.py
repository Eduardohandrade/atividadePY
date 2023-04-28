#Um motorista deseja colocar no tanque do seu carro X reais de gasolina. 
#Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu
#colocar no tanque.
preco_gasolina = float(input("Digite o preço do litro da gasolina: "))
valor_pagamento = float(input("Digite o valor do pagamento: "))

litros = valor_pagamento / preco_gasolina

print("Com", valor_pagamento, "reais, é possível colocar", litros, "litros de gasolina no tanque do carro.")
