valores = []

for cont in range (0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

for l, v in enumerate(valores):
    print(f'O maior valor é {max(valores)} e foi digitado na posição {valores.index(max(valores))}')
    print(f'O menor valor é {min(valores)} e foi digitado na posição {valores.index(min(valores))}')
    break
