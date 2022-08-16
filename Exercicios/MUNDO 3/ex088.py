from random import randint
import time
mega = []
jogo = []
print('-=' * 10)
print(f'{"MEGA DA VIRADA":^20}')
print('-=' * 10)
qsort = int(input('Quantos jogos você quer que eu sorteie?'))
for q in range(0, qsort):
    for s in range(0, 6):
        alea = randint(1, 60)
        if alea not in jogo:
            jogo.append(alea)
            mega.append(jogo[:])
            jogo.clear()
    mega.sort()
    print(f'Jogo {q +1}:{mega}', end='\n')
    mega.clear()
    time.sleep(1)
print(f'-=' * 5, '< BOA SORTE! >', '-=' * 5)
