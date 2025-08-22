import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]

i = 0
for i in range(10):
    random.shuffle(lista)
    i += 1
    print(i)
print('A ordem de apresentação será {}'.format(lista))