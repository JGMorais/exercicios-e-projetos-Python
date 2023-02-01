from random import randint
from time import sleep


def sorteia(list):
    print(f'Sorteando 5 valores da lista...', end='')
    for c in range(1, 6):
        n = randint(1, 10)
        list.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO')

def somap(list):
    soma = 0
    for valor in list:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores de pares de {list}, temos {soma}')


num = []
sorteia(num)
somap(num)
