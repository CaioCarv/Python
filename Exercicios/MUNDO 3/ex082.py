num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('*='*20)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
