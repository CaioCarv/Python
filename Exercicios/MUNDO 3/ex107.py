from modulos import moeda

v = int(input('Digite um preço: R$'))
moeda.lin()
print(f'A metade de {v} é {moeda.metade(v)}')
print(f'O dobro de {v} é {moeda.dobro(v)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(v, 10)}')
print(f'Reduzindo em 13%, temos {moeda.diminuir(v, 13)}')
moeda.lin()
