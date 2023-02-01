p = 0
tot = 0
m = 0
for c in range (1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    p = p + 1
    if ano < 2001:
        tot += 1
    else:
        m = p - tot
print('A todo temos {} pessoas maiores de idade.'.format(tot))
print('E tambem temos {} pessoas menores de idade.'.format(m))