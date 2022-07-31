from random import randint
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
print(f'\nO maior valor sorteado é {maior} e o menor foi o {menor}')

