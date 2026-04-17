import math
#from math import trunc#
num = float(input('Digite o número que você quer quebrar: '))

#print('O valor digitado foi {} e a porção inteira é {}'.format(num, int(num)))#
#print('O número digitado foi {} inteiro é {}'.format(num, math.trunc(num)))#



#não funciona da mesma forma, sempre arredonda para o sucessor, ex: 3.99
print('O número digitado foi {} inteiro é {:.0f}'.format(num, num))