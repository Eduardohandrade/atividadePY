Salario = float(input('digite seu salário:'))
Porcentagem1 = Salario*(15/100)
Salario_p1 = Salario+Porcentagem1
Porcentagem2 = Salario_p1*(8/100)
Salario_p2 = Salario_p1-Porcentagem2
print(f'Salario inicial era de {Salario} reais, com o acréscimo de 15% passou a ser {Salario_p1} reais, com o desconto dos imposto agora é de:{Salario_p2} reais')