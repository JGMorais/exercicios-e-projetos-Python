n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
escolha = 0
while escolha != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    escolha = int(input('Qual é a sua escolha?'))
    if escolha == 1:
        print('A soma dos numeros {} e {} é {}.'.format(n1, n2, (n1+n2)))
    elif escolha == 2:
        print('A multiplicação dos numeros {} e {} é {}.'.format(n1, n2, (n1*n2)))
    elif escolha == 3:
        if n1 > n2:
            print('O numero maior é {}'.format(n1))
        else:
            print('O numero maior é {}'.format(n2))
    elif escolha == 4:
        print('Digite Novamente!')
        n1 = int(input('Digite o primeiro numero:'))
        n2 = int(input('Digite o segundo numero:'))
    elif escolha == 5:
        print('Fim do programa!')
    else:
        print('Escolha invalida! Tente novamente!')


