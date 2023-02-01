total = totmil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp =='N':
        break
print('-'*15, 'FIM DO PROGRAMA', '-'*15)
print(f'O valor total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos com valor superior a R$ 1000')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')