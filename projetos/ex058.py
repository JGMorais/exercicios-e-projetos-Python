from random import randint
comp = randint(0, 10) #faz o computador escolher um numero
print('-=' * 30)
print('VOU PENSAR EM UM NUMERO ENTRE 0 E 10. TENTE ADIVINHAR...')
print('-=' *30)
acertou = False
pal = 0
while not acertou:
    jog = int(input('Qual é o seu palpite? '))
    pal += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Mais... Tente novamente!')
        elif jog > comp:
            print('Menos... Tente novamente!')
print('Acertou com {} palpites, PARABENS!!!'.format(pal))
