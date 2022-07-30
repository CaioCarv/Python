num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
option = int(input('Sua opção: '))
if option ==1:
    print('{} convertido em BINÁRIO é igual a {}'.format(num, bin(num)))
elif option ==2:
    print('{} convertido em OCTAL é igual a {}'.format(num, oct(num)))
elif option ==3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida. Tente novamente com outra opção')