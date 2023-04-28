Moeda1 = int(input('Moedas de 1 centavos:'))
Moeda5 = int(input('Moedas de 5 centavos:'))
Moeda10 = int(input('Moedas de 10 centavos:'))
Moeda25 = int(input('Moedas de 25 centavos:'))
Moeda50 = int(input('Moedas de 50 centavos:'))
Moeda11 = int(input('Moedas de 1 real:'))

moeda1 = Moeda1*0.01
moeda5 = Moeda5*0.05
moeda10 = Moeda10*0.10
moeda25 = Moeda25*0.25
moeda50 = Moeda50*0.50
moeda11 = Moeda11*11

total = moeda1+moeda5+moeda10+moeda25+moeda50+moeda11

print(f'Pedrinho, você economizou {total:.2f} reais.')