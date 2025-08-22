valor = float(input('Qual o preço do produto? R$'))
desc = (valor * 5) / 100

print('O novo valor do produto com o desconto de 5% é de R${}'.format(valor - desc))