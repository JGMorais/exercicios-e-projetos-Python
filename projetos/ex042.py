l1 = int(input('Digite o primeiro numero:'))
l2 = int(input('Digite o segundo numero:'))
l3 = int(input('Digite o terceiro numero:'))
if l2 + l3 > l1 and l1 + l3 > l2 and l1 + l2 > l3:
    print('Com os numeros {}, {}, e {} voce CONSEGUIU formar um Triangulo '.format(l1, l2, l3), end='')
    if l1 == l2 == l3:
        print('EQUILATERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Com os numeros {}, {}, e {} voce NÃO CONSEGUIU formar um Triangulo.'.format(l1, l2, l3))