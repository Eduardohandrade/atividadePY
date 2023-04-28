def quadrado(x):
    y = x * x 
    return y 

def love(a,b):
    print(f'{a} gosta de {b}')

valor_para_calculo=int(input('Digite um numero: '))
resultado = quadrado(valor_para_calculo)
print(resultado)

nome1=input('Nome 1: ')
nome2=input('Nome 2: ')
love(nome1,nome2)

