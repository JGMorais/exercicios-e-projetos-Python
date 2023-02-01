s = 0
c = 0
for d in range (1, 7):
    n = int(input('Digite o {} valor: '.format(d)))
    if n % 2 == 0:
        c = c + 1
        s = s + n
print('Voce informou {} numeros PARES e a soma foi {}'.format(c, s))