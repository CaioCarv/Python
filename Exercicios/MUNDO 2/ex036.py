casa = float(input('QUal o valor da casa?'))
salario = float(input('Qual é o seu salário?'))
anos = float(input('Em quantos anos o Sr. deseja pagar?'))

prestacao = casa / (anos * 12)
limite = salario * 0.3

if prestacao < limite:
    print('O salário do Sr. é {} e as parcelas serão {},'
          ' então está autorizado o seu empréstimo'.format(salario, prestacao))
else:
    print('O empréstimo do Sr. foi negado, pois a parcela de {}, está muito alta para o Senhor.'.format(prestacao))
