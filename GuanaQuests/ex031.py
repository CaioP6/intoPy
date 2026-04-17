dist = int(input('Qual é a distância da sua viagem? \n'))

if dist < 200:
    money = 0.50 * dist
elif dist >= 200:
    money = 0.45 * dist


print(f'''\nVocê está prestes a começar uma viagem de {dist}Km. 
      \nE o preço da sua passagem será de R${money:.2f}''')