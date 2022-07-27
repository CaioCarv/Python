print('GERADOR DE PA')
print('-=' * 10)
pritermo = int(input('Digite o primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = pritermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSE!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Foram usados {} termos'.format(cont))
print('FIM!!!')
