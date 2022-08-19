dic = {}

dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Média: '))
if dic['media'] >= 6:
    dic['situa'] = 'Aprovado'
else:
    dic['situa'] = 'Reprovado'
print(f'Nome é igual a {dic["nome"]}')
print(f'Média é igual a {dic["media"]}')
print(f'Situação é igual a {dic["situa"]}')
