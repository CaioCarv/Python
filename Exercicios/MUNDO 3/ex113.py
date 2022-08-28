def leiaFloat(msg):
    while True:
        try:
            v = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return v


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n = leiaInt('Digite um número inteiro: ')
v = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n}')
print(f'Você acabou de digitar o número real {v}')