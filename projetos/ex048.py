s = 0
c = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        c = c + 1
        s = s + n
print('A soma de todos os {} valores foi {}'.format(c, s))
