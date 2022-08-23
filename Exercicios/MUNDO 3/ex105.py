def notas(*n, sit=False):
    """
    -> Função para analisar notas dos alunos.
    :param n: As notas
    :param sit: False or True
    :return: r
    """
    r = dic = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


dic = notas(4, 5, 6, 2, sit=True)
help(notas)