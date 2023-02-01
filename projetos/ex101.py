
def voto(ano):
    from datetime import date
    atual = date.today().year
    n = atual - ano
    if 18 < n < 65:
        return f'Com {n} anos: Voto Obrigatório!'
    if n < 18:
        return f'Com {n} anos: Não Vota!'
    if n > 65:
        return  f'Com {n} anos: Voto Opcional!'


nasc = int(input('Em que ano voce nasceu: '))
print(voto(nasc))