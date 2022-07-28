from random import randint
jogador = soma = cpu = cont = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Diga um valor: '))
    cpu = randint(0, 10)
    escolha = str(input('Par ou ímpar? [P/I]')).strip().upper()
    soma = cpu + jogador
    if escolha == 'I':
        final = soma % 2
        if final == 0:
            print('-'*20)
            print(f'Você jogou {jogador} e o computador {cpu}. TOTAL de {soma} DEU PAR!!')
            print('-'*20)
            print('Você Perdeu!!')
            print('-='*20)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            print('-'*20)
            break
        else:
            print('-'*20)
            print(f'Você jogou {jogador} e o computador {cpu}. TOTAL de {soma} DEU ÍMPAR!!')
            print('-'*20)
            print('Você Venceu!!')
            print('-='*20)
            cont += 1
    else:
        final = soma % 2
        if final == 1:
            print('-'*20)
            print(f'Você jogou {jogador} e o computador {cpu}. TOTAL de {soma} DEU ÍMPAR!')
            print('-'*20)
            print('Você Perdeu!')
            print('-='*20)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            print('-'*20)
            break
        else:
            print('-'*20)
            print(f'Você jogou {jogador} e o computador {cpu}. TOTAL de {soma} DEU PAR!')
            print('-'*20)
            print('Você Venceu!')
            print('-='*20)
            cont +=1
