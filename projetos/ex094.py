ficha = {}
galera = []
soma = media = 0
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if ficha['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    galera.append(ficha.copy())
    while True:
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas. ')
media = soma / len(galera)
print(f'B) A media de idade das pessoas é {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRADO >>')
