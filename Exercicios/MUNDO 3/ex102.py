def fatorial(a, show=False):
    """
    fatorial(n, show=Flase)
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show:(opcional) Mostrar ou nã a conta.
        :return: O valor do Fatorial de um número n.
    """
    n = 1
    if show == True:
        for v in range(a, 0, -1):
            n *= v
            if v != 1:
                print(f'{v}', end=' x ')
            else:
                print(f'{v}', end=' = ')
        return n
    else:
        for v in range(a, 0, -1):
            n *= v
        return n


help(fatorial)

