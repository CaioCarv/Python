from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
for n in numeros:
    print(f'{n}', end= ' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')






'''from random import randint
maior = soma = 0
print('Os valores sorteados foram: ', end='')
for aleat in range(1, 6):
    aleat = randint(1, 50)
    soma += 1
    print(aleat, end=' ')
    if soma == 1:
        maior = menor = aleat
    else:
        if aleat >= maior:
            maior = aleat
        if aleat <= menor:
            menor = aleat
print(f'\nO maior valor sorteado é {maior} e o menor foi o {menor}')'''