nota1 = float(input('Qual a nota da primeira prova? '))
nota2 = float(input('Qual a nota da segunda prova? '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Parabéns, sua nota foi {}, você está aprovado'.format(media))
elif media >= 5:
    print('Sua média foi {}, ainda terá a recuperação para tentar ser aprovado!'.format(media))
else:
    print('Infelizmente sua nota foi {}, você está reprovado'.format(media))

