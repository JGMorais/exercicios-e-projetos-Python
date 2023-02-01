n = int(input('Digite um numero: '))
c = n
f = 1
for n in range(0, n):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))