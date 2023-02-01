ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('1º Nota: '))
    n2 = float(input('2º Nota: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar? [S/N] '.upper()))
    if resp in 'Nn':
        break
print('-=' * 35)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar nota de qual aluno: (999 interrompe)'))
    if opc == 999:
        print('FINALIZADO!')
        break
    if opc >= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte sempre!')