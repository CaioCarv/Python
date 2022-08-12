'''teste = list()
teste.append('Caio')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Mayra'
teste[1] = 25
galera.append(teste[:])
print(galera)'''

'''galera = [['Caio', 23], ['Ana', 33], ['Mayra', 25]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''


totmai = totmen = 0
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maior de idade e {totmen} menor de idade.')