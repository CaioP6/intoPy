km = float(input('Digite a quantidade de Km percorridos: '))
dia = int(input('Digite a quantidade de dias percorridos: '))

precoTotal = (60 * dia) + (0.15 * km)

print('O total a pagar é de R${}'.format(precoTotal))