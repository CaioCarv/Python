def lin():
    print('-=' * 15)


def area(a, b):
    ter = a * b
    lin()
    print('     CONTROLE DE TERRENOS ')
    lin()
    print(f'LARGURA (m): {a}')
    print(f'COMPRIMENTO (m): {b}')
    print(f'A área de um terreno de {a}x{b} é de {ter:.1f}')
    lin()


area(4.75, 5.89)
