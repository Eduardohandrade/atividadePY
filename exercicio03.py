#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos
#(aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%,
#escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
percentual_distribuidor = 0.28
percentual_impostos = 0.45

custo_distribuidor = custo_fabrica * percentual_distribuidor
custo_impostos = custo_fabrica * percentual_impostos
custo_consumidor = custo_fabrica + custo_distribuidor + custo_impostos

print("O custo ao consumidor do carro é de R$", custo_consumidor)