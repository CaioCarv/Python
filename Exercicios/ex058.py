from random import randint
from time import sleep

jogador = 0
comput = 1
vezes = 0
print('-=*' * 15)
print('Vou pensar em um número entre 0 e 22. tente adivinhar...')
print('-=*' * 15)
comput = randint(0, 22)
while jogador != comput:
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    vezes += 1
    sleep(1)
    if jogador != comput:
        if jogador > comput:
            print("Menos... Tente outra vez.")
        else:
            print('Mais... Tente outra vez.')
    else:
        print('Parábens, você acertou com {} tentativas!!!'.format(vezes))

