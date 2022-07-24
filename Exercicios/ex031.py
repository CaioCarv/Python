viag = int(input('Qual a distancia da sua Viagem? '))
if (viag <= 200):
  pssg = viag * 0.50
  print('A passagem ficará em R${} '.format(pssg))
else:
  pssg = viag * 0.45
  print('A passagem ficará em R${} '.format(pssg))