pri = int(input('Primeiro termo:'))
raz = int(input('Razão:'))
dec = pri + (10 - 1) * raz
for c in range (pri, dec + raz, raz):
    print('{} '.format(c), end='- ')
print('ACABOU')