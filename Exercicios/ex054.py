from datetime import date
atual = date.today().year
maior = 0
menor = 0

for c in range (1, 5):
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
if idade >= 18:
    maior = maior + 1
else:
    menor = menor + 1

print('Maior {} e Menor {}'.format(maior, menor))


