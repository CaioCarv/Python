lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Este número já foi adicionado anteriormente!')
    r = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if r in 'N':
        break
print('-*'*30)
lista.sort(reverse=True)
print(f'Você digitou os valores {lista}')