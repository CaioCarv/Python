from random import randint
from time import sleep
list = []


def valores(* num):
    print('Sorteando 5 valores da lista: ', end=' ')
    par = 0
    for v in range(0, 5):
        sort = randint(1, 10)
        list.append(sort)
        if v == 0:
            soma = sort
        else:
            soma += sort
        if sort % 2 == 0:
            par += sort
        print(f'{sort}', end=' ')
        sleep(0.2)
    print('PRONTO!')
    print(f'A soma de todos valores {list} é {soma}')
    print(f'A soma dos valores pares é {par}')

valores()
