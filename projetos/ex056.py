somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totm20 = 0
for p in range (1, 5):
    print('-----{}ª PESSOA-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totm20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadeh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm20))