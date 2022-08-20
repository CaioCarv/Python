from time import sleep


def lin():
    print('-=' * 20)


def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for v in num:
        print(f'{v}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print()
    lin()


lin()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()