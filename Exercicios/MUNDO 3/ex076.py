listagem = ('Caderno', 2.50, 'Borracha', 0.50, 'Régua', 1.50,
            'Caneta', 3.00, 'Esquadro', 4.00, 'Cartolina', 0.75)
print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-'*30)