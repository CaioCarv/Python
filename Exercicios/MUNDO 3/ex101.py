from datetime import date


def voto():
    hoje = date.today().year
    ano = int(input('Em que ano você nasceu? '))
    data = hoje - ano
    if data < 16:
        print(f'Com {data} anos: VOTO NEGADO')
    elif data < 18 or data > 64:
        print(f'Com {data} anos: VOTO OPCIONAL')
    else:
        print(f'Com {data} anos: VOTO OBRIGATÓRIO')


voto()
