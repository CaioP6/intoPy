from hmac import new

salario = float(input(f'Qual é o salário do funcionário? R$'))


def aumento10_salario(salario):
    new_salario = salario + (salario * 0.10)
    print(new_salario)
    return new_salario

def aumento15_salario(salario):
    new_salario = salario + (salario * 0.15)

    print(new_salario)
    return new_salario

if salario >= 1250:

    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento10_salario(salario):.2f}')
else:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento15_salario(salario):.2f}')
