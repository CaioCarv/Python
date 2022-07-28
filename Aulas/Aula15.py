'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')'''

nome = 'Caio'
idade = 23
salario = 2752.00
print('O %s tem %d anos e ganha $%d.' % (nome, idade, salario)) #PYTHON 2
print('O {} tem {} anos e ganha ${}'.format(nome, idade, salario)) #PYTHON 3
print(f'O {nome:^10} tem {idade} anos e ganha ${salario:.2f}') #PYTHON 3.6+