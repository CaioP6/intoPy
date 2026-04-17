class Televisor:

    def __init__(self, fabri, modelo):
        self.fabricante = fabri
        self.modelo = modelo
        self.canalAtual = None
        self.listaCanal = []
        self.volume = 20

    def aumentaVol(self, valor):

        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuiVol(self, valor):

        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocaCanal(self, canal):
        if canal in self.listaCanal:
            self.canalAtual = canal

    def sintonizaCanal(self, canal):
        if canal not in self.listaCanal:
            self.listaCanal.append(canal)

class ControleRemoto:

    def __init__(self, tv):
        self.tv = tv

    def aumentaVol(self):
        self.tv.aumentaVol(90)

    def diminuiVol(self):
        self.tv.diminuiVol(90)

    def trocaCanal(self, canal):
        self.tv.trocaCanal(canal)

    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)



