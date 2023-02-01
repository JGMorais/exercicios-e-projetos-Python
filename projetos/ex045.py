from random import randint
from time import sleep

print('{:=^40}'.format('JOKENPÔ'))
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''ESCOLHA UMAS DAS OPÇÕES!
[0] Pedra
[1] Papel
[2] tesoura''')
jogad = int(input('Qual voce escolheu?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('=-' * 20)
print('O computador escolheu {}'.format(itens[comp]))
print('O jogador escolheu {}'.format(itens[jogad]))
print('=-' * 20)
if comp == 0: # computador escolheu pedra
    if jogad == 0:
        print('EMPATE')
    elif jogad == 1:
        print('JOGADOR VENCEU!')
    elif jogad == 2:
        print('JOGADOR PERDEU!')
    else:
        print('Opção invalida!')

elif comp == 1: # computador esclheu papel
    if jogad == 0:
        print('JOGADOR PERDEU!')
    elif jogad == 1:
        print('EMPATE')
    elif jogad == 2:
        print('JOGADOR VENCEU!')
    else:
        print('Opção invalida!')

elif comp == 2: # computador escolheu tesoura
    if jogad == 0:
        print('JOGADOR VENCEU!')
    elif jogad == 1:
        print('JOGADOR PERDEU!')
    elif jogad == 2:
        print('EMPATE')
    else:
        print('Opção invalida!')