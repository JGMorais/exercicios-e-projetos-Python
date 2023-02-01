def fatorial(num=1, show=False):
    """
    =>Calculo fatorial de um numero
    :param num: Numero a ser fatorado
    :param show: Se deve ou não mostrar o calculo
    :return: Quantidade de vezes da função
    """""
    f = 1
    for c in range(num, 0, -1):
         f *= c
         if show:
             print(c, end='')
             if c > 1:
                 print(' x ', end='')
             else:
                 print(' = ', end='')
    return f


num = int(input('Digite um numero: '))
print(fatorial(num, show=True))