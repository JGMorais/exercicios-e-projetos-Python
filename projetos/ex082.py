v = []
lp = []
li = []
while True:
    n = (int(input('Digite um numero: ')))
    v.append(n)
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if n % 2 == 0:
        lp.append(n)
    else:
        li.append(n)
    if resp == 'N':
        break
print(f'A lista completa é {v}')
print(f'A lista par é {lp}')
print(f'A lista impar é {li}')