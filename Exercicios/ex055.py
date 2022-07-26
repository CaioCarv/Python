maior = 0
menor = 0

for p in range (1, 6):
    peso = float(input('Qual é o seu peso? '))
    if p == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))