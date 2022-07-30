num = int(input('Digite um número:'))
uni = num // 1 % 10
dec = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(uni))
print('Decena: {}'.format(dec))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
