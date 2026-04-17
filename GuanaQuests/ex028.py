from random import randint
import colorama

pensa = randint(0, 5)
print('\033[33m -=- ' * 20 )
print('\nO computador está pensando em um número de 0 a 5...\n')
print(' -=- ' * 20)

def correto():
    print('\033[32m -!- ' * 20)
    print('\nDroga... eu perdi :(\n')
    print(' -!- ' * 20)
def incorreto():
    print('\33[31m -x- ' * 20)
    print('\nQue pena... EU GANHEI!!  >:D\n')
    print(' -x- ' * 20)


res = int(input('\nDigite um número que você acha que ele pensou: '))

if res == pensa:
        correto()
elif res > 5:
    print('\nTu é burro? \nÉ um número de 0 a 5')

else:
        incorreto()
