#Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. 
#Considere fixo o juro da poupança em 0,70% a. m.
valor_depositado = float(input("Digite o valor depositado: "))

juros = 0.007  # equivalente a 0,70% a.m.
valor_rendimento = valor_depositado * juros
valor_total = valor_depositado + valor_rendimento

print("Valor depositado: R$", valor_depositado)
print("Valor do rendimento após um mês: R$", valor_rendimento)
print("Valor total após um mês: R$", valor_total)