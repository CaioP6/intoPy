import math

catOp = float(input('Comprimento do cateto oposto: '))
catAd = float(input('Comprimento do cateto adjacente: '))

hipo = (catOp ** 2 + catAd ** 2) ** (1/2)
#hipo = math.hypot(catOp, catAd)
print('A hipotenusa é igual a {:.2f}'.format(hipo))