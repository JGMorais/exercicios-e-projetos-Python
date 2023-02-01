from datetime import date
atual = date.today().year
ano = int(input('Em que ano voce nasceu?'))
idade = atual - ano
if idade == 18:
    print('Voce tem {}, já esta na hora de se alistar!'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Voce tem {}, ainda faltam {} anos, para voce se alistar!'.format(idade, saldo))
    print('Voce devera se alistar em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Voce tem {}, já passou {} anos da hora de se alistar!'.format(idade, saldo))
    print('Voce deveria se alistar em {}'.format(ano))