from datetime import date
ficha = {}
ficha['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ficha['idade'] = date.today().year - ano
ficha['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['carteira'] > 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['salario'] = int(input('Salário: '))
    ficha['aposentadoria'] = ficha['contratação'] + 35 - date.today().year + ficha['idade']
    for i, v in ficha.items():
        print(f' - {i} tem o valor {v}')

else:
    for i, v in ficha.items():
        print(f' - {i} tem o valor {v}')