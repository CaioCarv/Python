escolha = 0
while escolha != 5:
        valor1 = float(input('Qual o primeiro valor: '))
        valor2 = float(input('Qual o segundo valor: '))

        print('''*-*-*-*-*-MENU-*-*-*-*-*-*
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA''')
        escolha = int(input('Qual a opção você deseja escolher? '))

        if escolha == 1:
            soma = valor1 + valor2
            print('A soma entre {} e {} é {}'.format(valor1, valor2, soma))

        elif escolha == 2:
            mult = valor1 * valor2
            print('A multiplicação entre {} e {} é {}'.format(valor1, valor2, mult))

        elif escolha == 3:
            if valor1 > valor2:
                maior = valor1
            else:
                maior = valor2
            print('O maior número é {}'.format(maior))

        elif escolha == 4:
            print('Okay!')

print('Muito obrigado por Jogar!')

