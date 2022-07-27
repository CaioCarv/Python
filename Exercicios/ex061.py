print('GERADOR DE PA')
print('-=' * 10)
pritermo = int(input('Digite o primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = pritermo
cont = 1
while cont <= 10:
    print('{} => '.format(termo))
    termo += raz
    cont += 1
print('Fim!')
