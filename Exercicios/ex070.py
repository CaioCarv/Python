tot = mais = 0
menor = 1000000
print('=-'*12)
print('LOJÃO DO CAIO')
print('=-'*12)

while True:
    name = str(input('Nome do produto: ')).upper().strip()
    price = float(input('Preço do produto: '))
    tot += price

    if price > 1000:
        mais += 1

    if price < menor:
        menor = price
        namebarato = name
    contin = str(input('Deseja continuar? [S/N]')).upper().strip()
    if contin == 'N':
        break
print(f'O total gasto em compras é {tot}.')
print(f'Tem {mais} produtos com mais de 1000 reais.')
print(f'O produto mais barato é a {namebarato}')
