n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

def menor():
    if (n1 < n2) and (n1 < n3):
        menor = n1

    elif (n2 < n1) and (n2 < n3):
        menor = n2

    elif (n3 < n1) and (n3 < n2):
        menor = n3

    return(menor)

def maior():
    if (n1> n2) and (n1> n3):
        maior = n1

    elif (n2> n1) and (n2> n3):
        maior = n2

    elif (n3 > n1) and (n3 > n1):
        maior = n3

    return(maior)

print(f'O maior número é {maior()} e  o menor número {menor()}')
