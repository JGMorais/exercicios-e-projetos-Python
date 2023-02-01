vel = int(input('Digite a velocidade do carro:'))
if vel <= 80:
    print('Dentro do limite de velocidade... Boa viagem!!!')
else:
    mul = (vel - 80) * 7
    print('Voce esta acima do limite de velocidade!!! Voce sera multado em R${:.2f}'.format(mul))