import datetime
from datetime import date
atual = date.today().year
ano = int(input('Qual ano voce nasceu?'))
idade = atual - ano
if idade <= 9:
    print('Voce tem {} anos, sua categoria é a MIRIM!'.format(idade))
elif 9 < idade <= 14:
    print('Voce tem {} anos, sua categoria é a INFANTIL!'.format(idade))
elif 14 < idade <= 19:
    print('Voce tem {} anos, sua categoria é a JUNIOR!'.format(idade))
elif 19 < idade <= 25:
    print('Voce tem {} anos, sua categoria é a SENIOR!'.format(idade))
elif  idade > 25:
    print('Voce tem {} anos, sua categoria é a MARTER!'.format(idade))