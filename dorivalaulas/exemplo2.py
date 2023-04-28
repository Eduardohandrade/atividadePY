x = 'Oi, como vai você?'
msg= ': ' + x + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

x = 'E ai?'
msg= ': ' + x + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

x = 'nãoconsigolernada, nãoconsigolernada'
msg= ': ' + x + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

x = input('Qual é a sua mensagem? ')
msg= ': ' + x + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

def mensagem(x):
    MSG='| '  + x + ' |'
    print('-'*len(MSG))
    print(MSG)
    print('-'*len(MSG))

mensagem('Oi, como vai você?!')
mensagem('E ai!')
mensagem('obabaooobabaoobabao')
mensagem(input('Qual é a sua mensagem? '))
