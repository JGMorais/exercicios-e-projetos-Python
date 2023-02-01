n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
nt = (n1, n2, n3, n4)
np = 0
print(f'Voce digitou os valores {nt}')
if 3 in nt:
    print(f'O valor 3 apareceu na posição {nt.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado!')
print(f'O valor 9 apareceu {nt.count(9)} vezes.')
print('Os valores pares digitados foram ', end='')
for n in nt:
    if n % 2 == 0:
        print(n, end=' ')


