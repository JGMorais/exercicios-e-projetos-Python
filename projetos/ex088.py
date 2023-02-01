from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('-'*30)
qnt = int(input('Quantos jogos voce quer fazer? '))
tot = 1
while tot <= qnt:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {qnt} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)


