valores = [[], []]

for c in range(1,8):
    nu = int(input(f'Digite o {c}º valor: '))
    if nu % 2 == 0:
        valores[0].append(nu)

    else:
        valores[1].append(nu)

print('=-'*30)
print(f'Os valores digitados foram {valores}')
print(f'Os valores PARES digitados foram {sorted(valores[0])}')
print(f'Os valores IMPARES digitados foram {sorted(valores[1])}')