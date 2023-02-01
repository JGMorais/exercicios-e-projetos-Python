v = []
while True:
    n = (int(input('Digite um numero: ')))
    if n not in v:
        v.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não adicionado.')
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('=-'*30)
print(f'Voce digitou os valores {sorted(v)}')
