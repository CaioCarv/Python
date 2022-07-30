sexo = 'q'
while sexo not in 'M' 'F':
    sexo = str(input('Qual é o seu sexo ? ')).upper().strip()
if sexo == 'M':
    print('Seu sexo é Masculino')
else:
    print('Seu sexo é Feminino')

