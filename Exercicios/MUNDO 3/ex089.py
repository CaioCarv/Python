print('=-'*10)
print('BANCO CARVAL')
print('=-'*10)
cont50 = cont20 = cont10 = cont1 = 0

saq = int(input('Qual valor você quer sacar? R$'))

while saq > 50:
    saq = saq - 50
    cont50 += 1
while saq > 20:
    saq = saq - 20
    cont20 += 1
while saq > 10:
    saq = saq - 10
    cont10 += 1
while saq >= 1:
    saq = saq - 1
    cont1 += 1
print(f'Total de {cont50} cédulas de R$50')
print(f'Total de {cont20} cédulas de R$20')
print(f'Total de {cont10} cédulas de R$10')
print(f'Total de {cont1} cédulas de R$1')
print('-='*20)
print('Volte sempre ao BANCO CARVAL! Tenha um bom dia!')

