from random import randint
from time import sleep
from operator import itemgetter
Jogador = {}
dado = {}
c = 0
venc = []
print('Valores Sorteados:')
for c in range(0, 5):
    c += 1
    dado = randint(1, 7)
    Jogador[c] = dado
    print(f' O jogador {c} tirou {dado}')
    sleep(1)
    venc = sorted(Jogador.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('Ranking dos Jogadores:')
for i, v in enumerate(venc):
    print(f'{i+1}º lugar: Jogador {v[0]} com {v[1]}.')

