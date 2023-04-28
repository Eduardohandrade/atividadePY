#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada dia.
#Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães 
#e bolos (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos
#para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e depois calcular quanto 
#arrecadou naquele dia e quanto deve guardar na poupança.
# Lendo as quantidades de pães e bolos vendidos
quantidade_paes = int(input("Digite a quantidade de pães vendidos: "))
quantidade_bolos = int(input("Digite a quantidade de bolos vendidos: "))

# Calculando o valor arrecadado
valor_paes = quantidade_paes * 0.12
valor_bolos = quantidade_bolos * 1.5
total_arrecadado = valor_paes + valor_bolos

# Calculando o valor a ser guardado na poupança
valor_poupanca = total_arrecadado * 0.1

# Exibindo os resultados
print("Valor arrecadado: R$ {:.2f}".format(total_arrecadado))
print("Valor a ser guardado na poupança: R$ {:.2f}".format(valor_poupanca))