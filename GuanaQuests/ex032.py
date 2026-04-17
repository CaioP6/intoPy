import datetime
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
data_completinha = datetime.date.today()
ano_atual = data_completinha.year





def analisa_data(ano): 
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        print(f'O ano {ano} é bissexto!')
        return

    else:
        print(f'O ano {ano} não é bissexto')
        return


if ano == 0:
    ano = ano_atual
    analisa_data(ano)
    
else:
    analisa_data(ano)