from intoPy.otherQuest.tvTest.funcionalidades import *

tv = Televisor('Sony', 'Sony-123')

controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canalAtual)
print(tv.volume)