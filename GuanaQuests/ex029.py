import random

vel = random.randint(40, 140)
limite = 80
print(f'A velocidade do carro é de {vel}Km/h')

def multa():

    print(f'\n\033[31mO carro ultrapassou o limite de {limite}km/h')
    print(' - ' * 20)
    print('A multa vai custar R$7,00 por cada Km acima do limite')
    print(f'\nA multa será de R${(vel - limite) * 7}')
    
def nada():
    print('\n\033[34mO carro não ultrapassou o limite de velocidade...')

if vel > limite:
    multa()
else:
    nada()

