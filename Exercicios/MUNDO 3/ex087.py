matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
col = mai = par = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite [{l}, {c}]: '))
        if c == 2:
            col += matriz[l][c]
        if matriz[l][c] %2 == 0:
            par += matriz[l][c]
        if l == 1 and matriz[l][c] > mai:
            mai = matriz[l][c]
print('*=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('*=' * 30)
print(f'A soma de valores da terceira coluna é {col}')
print(f'A soma dos pares é {par}')
print(f'O maior valor da segunda linha é {mai}')
