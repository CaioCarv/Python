num = [2, 5, 9, 1, 8, 4]
num[2] = 3
num.append(7)
num.sort()
num.insert(2, 0)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')


valores = []
for cont in range (0, 4):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')



a = [2, 3, 4, 6]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')