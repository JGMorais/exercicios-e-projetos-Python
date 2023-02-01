from random import randint
v = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Voce jogou {jog} e o computador {comp}. Total de {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')