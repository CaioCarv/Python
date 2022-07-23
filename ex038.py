valor = float(input('Qual primeiro valor? '))
valor2 = float(input('Qual o segundo valor? '))

if valor > valor2:
    print('O primeiro valor {}, é maior!'.format(valor))
elif valor < valor2:
    print('O segundo valor {}, é maior!'.format(valor2))
else:
    print('Os valores são iguais! {}'.format(valor))
