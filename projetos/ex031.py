dist= float(input('qual é a distancia da sua viagem?'))
print('Voce esta prestes a começar uma viagem de {}Km.'.format(dist))
if dist <=200:
    preco = dist * 0.50
else:
    preco = dist *0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))