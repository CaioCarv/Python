from time import sleep


def sep():
    print('-=' * 20)


def contadorA():
    for c in range(1, 11, 1):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


def contadorB():
    for c in range(10, 0, -2):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


def contadorC():
    print('Agora é sua vez de personalizar a contagem!')
    start = int(input('Start: '))
    end = int(input('End: '))
    step = int(input('Step: '))
    if step == 0:
        step = 1
    if start > end:
        step = -step
    for c in range(start, end, step):
        print(c, end=' ')
        sleep(0.5)
    print(f'{end} FIM!')


sep()
print(f'Contagem de 1 até 10 de 1 em 1')
contadorA()
print()
sep()
print(f'Contagem de 10 até 0 de 2 em 2')
contadorB()
print()
sep()
contadorC()
print()
sep()
