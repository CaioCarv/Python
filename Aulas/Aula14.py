'''for c in range (1, 10):
  print(c)
print('Fim')'''

'''r = 'S'
while r == 'S':
  n = int(input('Digite um valor: '))
  r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim!')'''
impar=0
par=0
n = 1
while n != 0:
  n = int(input('Digite um valor: '))
  if n % 2 == 0:
    par += 1
  else:
    impar += 1
print('Você digitou {} números par e {} números impares'.format(par, impar))
