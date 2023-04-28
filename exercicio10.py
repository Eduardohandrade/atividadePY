#Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas
# por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome,
# o salário fixo e salário no final do mês.
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas pelo vendedor: "))

comissao = 0.15 * total_vendas
salario_final = salario_fixo + comissao

print("Nome do vendedor:", nome_vendedor)
print("Salário fixo:", salario_fixo)
print("Comissão sobre vendas:", comissao)
print("Salário final:", salario_final)