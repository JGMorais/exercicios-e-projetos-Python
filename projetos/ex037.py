num = int(input('Digite um numero:'))
print('''Escolha uma Base de Conversão!
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opção = int(input('Qual voce escolheu?'))
if opção == 1:
    print('O numero digitado foi {} e na base binaria fica {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O numero digitado foi {} e na base octal fica {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O numero digitado foi {} e na base hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    opção == 0
    print('Opção de ecolha ERRADA, escolha novamente!')
