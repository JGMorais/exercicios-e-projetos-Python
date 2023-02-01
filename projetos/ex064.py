n = c = s = 0
n = int(input('Digite um numero ou [999] para parar: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um numero ou [999] para parar: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(c, s))