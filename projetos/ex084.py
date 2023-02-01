galera = []
dado = []
ma = me = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        ma = me = dado[1]
    else:
        if dado[1] > ma:
            ma = dado[1]
        if dado[1] < me:
            me = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('=-'*25)
print(f'Ao todo voce cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {ma}Kg. Peso de ', end='')
for p in galera:
    if p[1] == ma:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {me}Kg. Peso de ', end='')
for p in galera:
    if p[1] == me:
        print(f'{p[0]}', end='')
print()