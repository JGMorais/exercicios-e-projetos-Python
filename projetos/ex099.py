def maior(* num):
    cont = maior = 0
    print('-='*25)
    print('Analizando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram passados {cont} valores ao todo.')
    print(f'O maior valor informado foi o {maior}')


maior(2, 3, 5, 8, 9)
maior(6, 5, 7)
maior(9)
maior()

