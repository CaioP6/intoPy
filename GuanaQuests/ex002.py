#lista
mochila = ['corda', 'faca', 'garrafa']
#add item
mochila.append('maçã')
#remove item
mochila.remove('maçã')

#iteração dos itens da mochila, enumerate fornece tanto o índice quanto o valor
def AbrirMochila():

    for indice, item in enumerate (mochila):
        print('Indíce {}: {}'.format(indice, item))

    print('\nQuantidade de itens: {}'.format(len(mochila)))

def Add():
    novo_item = input('Escreva qual item deseja colocar na mochila: ')
    mochila.append(novo_item)

def Rem():
    remove = input('Digite o item que deseja largar: ')
    mochila.remove(remove)

quest = None

while quest != 'sim' or quest != 'Sim':
    quest = input('Deseja abrir a mochila?\n')

    if quest == 'sim' or quest == 'Sim':
        print('\n')
        AbrirMochila()
        action = input('\nDigite a ação que deseja fazer: \nFechar a mochila\nGuardar um item na mochila\nTirar um item da mochila\n\n')

        if action == 'Fechar' or action == 'fechar' or action == 'fechar a mochila' or action == 'Fechar a mochila':
                exit()

        if action == 'Guardar' or action == 'guardar' or action == 'guardar um item na mochila' or action == 'Guardar um item na mochila':
            Add()

        if action == 'Tirar' or action == 'tirar' or action == 'Tirar um item da mochila' or action == 'tirar um item da mochila':
            Rem()

    if quest == 'não' or quest == 'Não' or quest == 'nao' or quest == 'Nao':
        exit()


