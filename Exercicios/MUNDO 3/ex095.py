futebol = {}
partidas = []
time = []
while True:
    futebol.clear()
    futebol['nome'] = str(input('Nome:'))
    part = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
    partidas.clear()
    for j in range(0, part):
        partidas.append(int(input(f'    Quantos gols na {j+1}° partida: ')))
    futebol['gols'] = partidas[:]
    futebol['total'] = sum(partidas)
    time.append(futebol.copy())
    while True:
        resp = str(input('Quer continuar ? {S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in futebol.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:^3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)
while True:
    busc = int(input('Mostrar dados de qual jogador? '))
    if busc == 999:
        break
    if busc >= len(time):
        print(f'ERRO! Não existe jogador com código {busc}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busc]["nome"]}:')
        for i, g in enumerate(time[busc]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-=' * 30)
print('<<VOLTE SEMPRE>>')
