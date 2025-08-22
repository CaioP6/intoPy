cont = str(input('Digite uma frase: ')).strip()
letra = str(input('Digite a letra que deseja analisar: ')).lower()

print(f'A letra {letra} aparece {cont.count(letra.lower())} vezes')
print(f'A letra {letra} aparece primeiro na posição {cont.find(letra) + 1}')#find procura a primeira posição em que a letra aparece
print(f'A última posição da letra {letra} é a posição {cont.strip().rfind(letra) + 1}') #rfind procura da direita pra esquerda

