peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))

imc = peso / ( altura * altura)

if imc > 40:
    print('Seu IMC é {:.2f}, tu é gordo pra krlh em, cuidado! "mórbida"'.format(imc))
elif imc > 30:
    print('Seu IMC é {:.2f}, tu é gordão, mas vai! "Obesidade"'.format(imc))
elif imc > 25:
    print('Seu IMC é {:.2f}, tu é fofinho apenas! "Sobrepeso"'.format(imc))
elif imc > 18.5:
    print('Seu IMC é {:.2f}, Ta em forma em galã! "Peso ideal"'.format(imc))
else:
    print('Seu IMC é {:.2f}, Se bater um vento você voa mlk! "Abaxio do Peso"'.format(imc))
