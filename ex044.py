valor = float(input('Qual o valor do produto ?'))
pagar = int(input('Como deseja pagar ? (1-Dinheiro) (2-Cartão)'
                   '(3- 2x no cartão) (4- 3x ou mais): '))
if pagar == 1:
    final = valor - (valor * 0.10)
    print('O valor pago será {}'.format(final))
elif pagar == 2:
    final = valor - (valor * 0.05)
    print('O valor pago será {}'.format(final))
elif pagar == 3:
    print('O valor pago será {}'.format(valor))
else:
    final = valor + (valor * 0.20)
    print('O valor pago será {}'.format(final))