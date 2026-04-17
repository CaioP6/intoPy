valor_casa = float(input(f'Insira o valor da casa: R$'))
salario = float(input(f'Insira o seu salário: R$'))
anos = int(input(f'Insira a quantidade de anos em que irá pagar: '))

salario30 = salario * 0.30
qtd_mes = anos * 12
prestacao = valor_casa / qtd_mes

if prestacao > salario30:
    print(f'''\nPara pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}
            Empréstimo NEGADO!''')
else:
    print(f'\nPara pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}'
          f'\nEmpréstimo APROVADO!''')
