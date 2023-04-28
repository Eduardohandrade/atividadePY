#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros.
# Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
valor_compra = float(input("Digite o valor da compra: "))

num_prestacoes = 5
valor_prestacao = valor_compra / num_prestacoes

print("Valor da compra: R$", valor_compra)
print("Valor de cada prestação: R$", valor_prestacao)