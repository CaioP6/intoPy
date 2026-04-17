num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')

print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opt = int(input('Sua opção: '))

if opt == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {num:X}')