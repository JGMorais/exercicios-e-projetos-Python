valor = float(input('Digite o valor do produto R$:'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x na cartão
[4] 3x no cartão''')
opcao = int(input('Qual a opção de compra?'))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parc = valor / 2
    print('Sua compra ficou parcelada em 2x de R${:.2f} com total de R${:.2f} sem JUROS.'.format(parc, valor))
elif opcao == 4:
    total = (valor + (valor * 20 / 100))
    parc = int(input('Quantas parcelas?'))
    totpar = total / parc
    print('Sua compra ficou parcelada em {} de R${:.2f} com valor total de R${:.2f} com 20% de JUROS.'.format(parc, totpar, total))
else:
    opcao = 0
    total = valor
    print('Opção invalida de pagamento!')
print('Sua compra de R${:.2f} ficou R${:.2f}.'.format(valor, total))





