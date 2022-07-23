anos = int(input('Quantos anos você tem?'))

if anos == 18:
    print('Este ano você terá que se apresentar para os serviços militares recruta 022!')
elif anos > 18:
    soma = anos - 18
    print('Você deveria ter se alistado a {} anos atrás seu mocorongo!'.format(soma))
else:
    sub = 18 - anos
    print('Seu precoce, ainda falta {} anos, para você ir capinar lote!'.format(sub))
