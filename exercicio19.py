Quantidade_sanduiche= int(input('Quantidade de sanduiche:'))
queijo = Quantidade_sanduiche*100
presunto = Quantidade_sanduiche*50
hambúrguer = Quantidade_sanduiche*100

queijokg = queijo/1000
presuntokg = presunto/1000
hambúrguerkg = hambúrguer/1000

print(f'Para {Quantidade_sanduiche} Sanduíches será gasto:\n{queijokg}kg de queijo\n{presuntokg} kg de presuntos\n{hambúrguerkg} kg de hambúrguer')
