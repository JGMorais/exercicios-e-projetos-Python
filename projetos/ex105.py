def notas(*n, sit=False):
    """
    => Função para analisar notas e situação de varios alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'BOA!'
        elif r['media'] >= 5:
            r['Situação'] = 'RAZOAVEL!'
        else:
            r['Situação'] = 'RUIM!'
    return r


resp = notas(5, 8, 6, 10, sit=True)
print(resp)


