mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = 0
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um valor para [{l}], [{c}]: '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
        if mat[l][c] % 2 == 0:
            sp += mat[l][c]
    print()
soma = mat[0][2] + mat[1][2] + mat[2][2]
print(f'A soma dos valores PARES é {sp}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior da segunda coluna é {max(mat[1])}')
