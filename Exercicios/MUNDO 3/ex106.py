c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;45m',
     '\033[7;30m'
     )


def ajuda():
    while True:
        print('*' * 20)
        aj = str(input(f'{c[2]}Função ou biblioteca >')).strip().lower()
        print(c[0])
        print(f'*' * 20)
        if aj == 'fim':
            print(f'{c[3]}ATÉ LOGO')
            break
        tex = help(aj)


ajuda()