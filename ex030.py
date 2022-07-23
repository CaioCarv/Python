num = int(input('Digite um número: '))
result = num %2
if (result == 0):
  print('{} é PAR'.format(num))
else:
  print('{} é IMPAR'.format(num))