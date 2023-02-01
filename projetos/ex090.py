ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {"nome"}: '))
if ficha['media'] >= 7:
    ficha['situação'] = 'APROVADO'
elif 5 <= ficha['media'] < 7:
    ficha['situação'] = 'RECUPERAÇÃO'
else:
    ficha['situação'] = 'REPROVADO'
print('-='*30)
for k, v in ficha.items():
    print(f' {k} é igual a {v}')

