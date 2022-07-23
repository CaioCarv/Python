km = float(input('Quantos KM foi rodado?'))
dia = float(input('Quantos dias foram alugados?'))

kmR = (km * 0.15)
diaR = (dia * 60)
tot = (kmR + diaR)
print('----TABELA DE ALUGUEL----')
print('O total que você terá que pagar é {:.2f}'.format(tot))
