resp = 'S'
s = q = m = ma = me = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    s += n
    q += 1
    if q == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
m = s / q
print('Voce digitou {} numeros e a media foi {}'.format(q, m))
print(f'O maior valor foi {ma} e o menor foi {me}')

