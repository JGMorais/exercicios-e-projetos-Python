import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'A dobro de {moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando em 10% de {moeda.moeda(p)} é R${moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 10% de {moeda.moeda(p)} é R${moeda.moeda(moeda.diminuir(p, 10))}')