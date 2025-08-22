carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = carteira / 5.49
print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira, dolar))