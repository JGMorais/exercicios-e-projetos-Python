casa = float(input('Digite o valor da casa R$:'))
salario = float(input('Qual é o seu salario? R$:'))
anos = int(input('Em quantos anos voce pretende pagar?'))
mensal = casa / (anos * 12)
minimo = salario * 30 / 100
if minimo <= mensal:
    print('Com um salario de R${:.2f} e o valor da casa de R${:.2f} a prestação fica R${:.2f}'.format(salario, casa, mensal))
    print('Sua compra foi NEGADA!')
else:
    print('Com um salario de R${:.2f} e o valor da casa de R${:.2f} a prestação fica R${:.2f}'.format(salario, casa, mensal))
    print('Sua compra foi APROVADA!')