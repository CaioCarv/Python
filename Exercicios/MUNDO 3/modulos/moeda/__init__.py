def lin():
    print('-' * 40)


def metade(v=0, formato=False):
    res = v / 2
    return res if formato is False else moeda(res)


def dobro(v=0, formato=False):
    res = v * 2
    return res if not formato else moeda(res)


def aumentar(v=0, n=0, formato=False):
    res = v + (v * n / 100)
    return res if not formato else moeda(res)


def diminuir(v=0, n=0, formato=False):
    res = v - (v * n / 100)
    return res if formato is False else moeda(res)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')


def resumo(v=0, na=10, nr=15):
    lin()
    print('RESUMO DO VALOR'.center(40))
    lin()
    print(f'Preço analisado: \t{moeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'{na}% de aumento: \t{aumentar(v, na, True)}')
    print(f'{nr}% de redução: \t{diminuir(v, nr, True)}')
