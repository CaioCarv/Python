maior = homens = menor20 = 0
print('-------------------')
print('CADASTRE UMA PESSOA')
print('-------------------')
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menor20 += 1
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
    else:
        print('-------------------')
        print('CADASTRE UMA PESSOA')
        print('-------------------')
print(f'Maior de idade tem {maior}, homens contém {homens} '
      f'e mulheres com menos de 20 anos são {menor20}')

