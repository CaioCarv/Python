from datetime import date
atual = date.today().year
nasc = int(input('Qual de nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Este ano você terá que se apresentar para os serviços militares recruta 022!')
elif idade > 18:
    soma = idade - 18
    print('Você deveria ter se alistado a {} anos atrás seu mocorongo!'.format(soma))
else:
    sub = 18 - idade
    print('Seu precoce, ainda falta {} anos, para você ir capinar lote!'.format(sub))


