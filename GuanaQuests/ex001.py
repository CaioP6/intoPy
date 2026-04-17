n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('\nSoma'
      '\nSubtração'
      '\nMultiplicação'
      '\nDivisão\n')

opera = input('Qual operação deseja realizar? \n')


def somar(n1, n2):
    resul = n1 + n2
    print('\nO resultado da soma é {:.0f}.'.format(resul))

def subtrair(n1, n2):
    resul = n1 - n2
    print('\nO resultado da subtração é {:0f}.'.format(resul))

def divisao(n1, n2):
    resul = n1 / n2
    print('\nO resultado da divisão é {}.'.format(resul))

def multi(n1, n2):
    resul = n1 * n2
    print('\nO resultado da multiplicação é {}.'.format(resul))


if opera == 'Soma' or opera == 'soma' or opera == '+' or opera == '1':
    somar(n1, n2)

if opera == 'Subtração' or opera == 'subtração' or opera == '-' or opera == '2':
    subtrair(n1, n2)

if opera == 'Multiplicação' or opera == 'multiplicação' or opera == 'x' or opera == '*' or opera == '3':
    multi(n1, n2)

if opera == 'Divisão' or opera == 'divisão' or opera == '/' or opera == '4':
    divisao(n1, n2)


