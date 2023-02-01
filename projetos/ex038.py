a = int(input('Digite o primeiro numero:'))
b = int(input('Digite o segundo numero:'))
if a == b:
    print('Não há numeros maior, os dois são iguais.')
elif a > b:
    print('O numero {} é maior que {}.'.format(a, b))
elif b > a:
    print('O numero {} é maior que {}.'.format(b, a))