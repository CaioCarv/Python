list = []
listFem = []
listIda = []
cad = tot = 0
while True:
        pessoa  = {}
        pessoa['n'] = str(input('Nome: '))
        pessoa['s'] = str(input('sexo: [M/F]')).upper().strip()
        pessoa['i'] = int(input('Idade: '))
        list.append(pessoa)
        if pessoa['s'] == 'F':
                listFem.append(pessoa['n'])
        if pessoa['i'] >= 30:
                listIda.append(pessoa['n'])
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()
        cad += 1
        tot = (tot + pessoa['i']) / cad
        if resp == 'N':
                break
print('=-' * 20)
print(f'Foram cadastradas {cad} pessoas')
print(f'A média de idade do grupo é {tot}')
print(f'As mulheres são: {listFem}')
print(f'Acima da idade está {listIda}')
print('=-' * 20)
