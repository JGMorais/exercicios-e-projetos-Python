jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
gol = []
jog = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, jog):
    c += 1
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gol'] = gol
    jogador['total'] = sum(jogador['gol'])


print('-='*30)
print(jogador)
print('-='*30)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jog} partidas.')
for c in range(0, jog):
    c += 1
    print(f'=> Na partida {c}, fez {jogador["gol"][c-1]}')
print(f'Foi um total de {jogador["total"]}')