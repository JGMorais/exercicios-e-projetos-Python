p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
c = 1
t = p
m = 10
to = 0
while m != 0:
    to = to + m
    while c <= to:
        print('{}'.format(t), end='')
        print(' - ' , end='')
        t += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos voce quer ver a mais? '))
    if m == 0:
        print('Progressão finalizada com {} termos.'.format(to))

