#1- A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
#∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
#∆t: variação de tempo (tempo final – tempo inicial) em horas
#Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  

Ds = float(input('Variaçao de espaço (ponto de chegada - ponto de partida) em km: '))
Dt = float(input('Variaçao de tempo (tempo inicial - tempo final) em horas:'))
Vm = Ds/Dt 
print(f'A velocidade media do veiculo e de {Vm:2f}')