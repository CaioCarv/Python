maior = homens = menor20 = 0
print('-------------------')
print('CADASTRE UMA PESSOA')
print('-------------------')
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menor20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
    else:
        print('-------------------')
        print('CADASTRE UMA PESSOA')
        print('-------------------')
print(f'Maior de idade tem {maior}, homens contém {homens} '
      f'e mulheres com menos de 20 anos são {menor20}')

