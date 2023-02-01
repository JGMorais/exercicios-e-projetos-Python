import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'A dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando em 10% de {moeda.moeda(p)} é {moeda.aumentar(p, 10,True)}')
print(f'Diminuindo em 10% de {moeda.moeda(p)} é {moeda.diminuir(p, 10,True)}')