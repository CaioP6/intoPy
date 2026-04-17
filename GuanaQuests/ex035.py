print('-=-' * 10)
print(' ' * 2, 'Analisador de Triângulos')
print('-=-' * 10)

seg_1 = float(input('Primeiro segmento: '))
seg_2 = float(input('Segundo segmento: '))
seg_3 = float(input('Terceiro segmento: '))



if seg_1 < seg_2 + seg_3 and seg_2 < seg_3 + seg_2 and seg_3 < seg_3 + seg_1:
    print(f'Os segmentos inseridos formam um triângulo')
else:
    print(f'Os segmentos não formam um triângulo')