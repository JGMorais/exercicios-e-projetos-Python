v = []
while True:
    n = (int(input('Digite um numero: ')))
    v.append(n)
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
v.sort(reverse=True)
print(f'Voce digitou {len(v)} elementos')
print(f'Os valores em ordem decrescente são {v}')
if 5 in v:
    print('O valor 5 consta na lista.')
else:
    print('Não consta o valor 5 na lista.')