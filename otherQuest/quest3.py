import math

class Esfera:

    def __init__(self, cor, raio):

        self.cor = cor
        self.raio = raio

    def volume(self):

        vol = (4/3) * math.pi * (self.raio ** 3)

        return vol

    def area(self):

        ar =  4 * math.pi * (self.raio ** 2)

        return ar

cor = str(input('Digite uma cor: '))
raio = float(input('\nDigite um raio: '))
bola = Esfera(cor, raio)

print('O volume da bola é {:.2f}cm³, e sua área é {:.2f}cm²'.format(bola.volume(), bola.area()))
print('\nE a cor é {}'.format(bola.cor))


