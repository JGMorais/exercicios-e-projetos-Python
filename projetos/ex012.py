p= float(input('Digite o valor do produto:'))
pn= p-(p*5/100)
print('O valor do seu produto sem desconto é R${:.2f} e com o desconto de 5% ficou R${:.2f}.'.format(p, pn))
