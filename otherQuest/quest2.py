#sequência de fibonacci(0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)

def validar_num(n1):

    fibonacci = [0, 1]
    while fibonacci != n1:
        prox_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(prox_num)
    return fibonacci

n1 = int(input('Insira um número: '))
resultado = validar_num(n1)
print(resultado)