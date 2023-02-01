def aumentar(preco=0, taxa=0, formatado=True):
    res = preco + (preco * taxa / 100)
    return res if formatado is False else moeda(res)


def diminuir(preco=0, taxa=0, formatado=True):
    res = preco - (preco * taxa / 100)
    return res if formatado is False else moeda(res)


def dobro(preco=0, formatado=True):
    res = preco * 2
    return res if not formatado else moeda(res)


def metade(preco=0, formatado=True):
    res = preco / 2
    return res if not formatado else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, a=aumentar(), b=diminuir()):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Dobro do preço:\t\t{dobro(preco)}')
    print(f'Metade do preço:\t{metade(preco)}')
    print(f'{a}% de aumento:\t\t{aumentar(preco, a)}')
    print(f'{b}% de redução:\t\t{diminuir(preco, b)}')



