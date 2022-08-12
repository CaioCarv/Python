pessoa = []
grupo = []
mai = men = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    c = str(input('Deseja continuar? [S/N]')).strip().upper()
    if c == 'N':
        break
print('=*'*15)
print(f'Foram cadastradas {len(grupo)} pessoas!')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == mai:
        print(f'[{p[0]}]' , end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
