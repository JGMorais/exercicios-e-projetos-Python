sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso!'.format(sexo))
