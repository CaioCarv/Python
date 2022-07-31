valor = int(input('Digite um valor: ' ))
valor2 = int(input('Digite mais um valor: '))
valor3 = int(input('Digite outro valor: '))
valor4 = int(input('Digite o último valor: '))
tup = (valor, valor2, valor3, valor4)
soma = 0
for som9 in tup:
    if som9 == 9:
        soma += 1
    if som9 == 3:
        print(f'O número 3 está {enumerate(tup)}')
        break
    if som9 % 2 ==0:
        par = (som9)
print(f'Os números pares foram {par}')
print(f'Apareceu {soma} vezes o número 9!')
