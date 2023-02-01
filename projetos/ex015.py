d = float(input('Quantos dias o carro ficou alugado: '))
km = float(input('Quantos KM foi percorrido: '))
p = d * 60 + 0.15 * km
print('O Valor total a ser pago do aluguel do carro é: R${:.2f}'.format(p))