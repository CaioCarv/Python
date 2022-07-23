"""nome = str(input('Qual é seu nome? '))
if nome == 'Caio':
  print('Que nome lindo você tem!'.format(nome))
else:
  print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Dugute a segunda nota: '))
n = (n1 +n2)/2
print('A sua média foi {:.1f}'.format(n))
if n >= 6.0:
  print('Sua média foi boa! PARABÉNS!!!')
else:
  print('Sua média foi ruim! ESTUDE MAIS!!!')