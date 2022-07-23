vel = int(input('Qual a velocidade atual? '))
multa = (vel - 80)
pagar = (multa * 7)
if (vel > 80):
  print('Você foi multado por excesso de velocidade!')
  print('A multa vai custar R${}'.format(pagar))
else: 
  print('Tenha um bom dia! Dirija com cuidado!')