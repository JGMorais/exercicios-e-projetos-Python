from random import randint
from time import sleep
comp = randint(0, 5) #faz o computador escolher um numero
print('-=' * 30)
print('VOU PENSAR EM UM NUMERO ENTRE 0 E 5. TENTE ADIVINHAR...')
print('-=' *30)
jog = int(input('Em que numero pensei?')) # jogador tenta adivinhar
print('Processando...')
sleep(1)
if jog == comp:
    print('PARABENS!!! VOCE ME VENCEU!!!')
else:
    print('GANHEI!!! PENSEI NO NUMERO {}'.format(comp))