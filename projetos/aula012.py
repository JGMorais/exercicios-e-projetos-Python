nome = str(input('Qual é o seu nome?'))
if nome == 'João':
    print('Que nome bonito!')
elif nome == 'Pedro' or 'Maria' or 'Jessica':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Leticia Mariana':
    print('Que belo nome Feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))