print('=-='*15)
print('{:^40}'.format('TABELA DO BRASILEIRÃO'))
print('=-='*15)
times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG',
      'Santos', 'América-MG', 'Goiás', 'Bragantino', 'Fortaleza', 'São Paulo', 'Botafogo', 'Ceará',
      'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
print(f'Os cinco primeiros são {times[:5]}')
print(f'Os quatro ultimos times são {times[-4:]}')
print(sorted(times))
print(f'O time do Corinthians esta na posição {times.index("Corinthians")+1}ª')