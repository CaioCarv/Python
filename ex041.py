idade = int(input('Qual ano de nascimento do atleta: '))
categoria = 2022 - idade

if categoria > 20:
    print('A sua categoria é Master')
elif categoria > 18:
    print('A sua categoria é Sênior')
elif categoria > 14:
    print('A sua categoria é Junior')
elif categoria > 9:
    print('A sua categoria é infantil')
else:
    print('A sua categoria é mirim')
