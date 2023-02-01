n = []
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c} : ')))
print('=-'*25)
print(f'Voce digitou os valores {n}')
print(f'O maior valor digitado foi {max(n)} na posições ', end='')
for i, v in enumerate(n):
    if v == (max(n)):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(n)} na posição ', end='')
for i, v in enumerate(n):
    if v == (min(n)):
        print(f'{i}...', end='')
print()

