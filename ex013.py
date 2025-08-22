salario = float(input('Qual é o salário do funcionário? R$'))
aum = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${}'.format(salario, aum))