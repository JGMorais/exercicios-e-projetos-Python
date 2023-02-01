print('='*40)
print('{: ^40}'.format('BANCO JOTA'))
print('='*40)
valor = int(input('Que valor voce deseja sacar? R$ '))
notas = 0
ced = 50
total = valor
while True:
    if total >= ced:
        total -= ced
        notas += 1
    else:
        if notas > 0:
            print(f'Total de {notas} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        notas = 0
        if total == 0:
            break
print('='*40)
print('{: ^40}'.format('OBRIGADO! VOLTE SEMPRE!'))
print('='*40)









