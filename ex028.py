from random import randint
from time import sleep
comput = randint(0, 5)
print('-=*' * 15)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=*' * 15)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if (comput == jogador): 
  print('Você acertou!')
else:
  print('Voçê errou!')
