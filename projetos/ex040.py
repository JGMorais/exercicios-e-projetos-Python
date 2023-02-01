n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if 7 > media >= 5:
    print('Sua media é {}, voce ficou de RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua media foi de {}, voce foi APROVADO!'.format(media))
elif media < 5:
    print('Sua media foi de {}, voce esta REPROVADO!'.format(media))