futebol = {}
partidas = []
futebol['nome'] = str(input('Nome:'))
part = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
for j in range(0, part):
    partidas.append(int(input(f'    Quantos gols na {j+1}° partida: ')))
futebol['gols'] = partidas[:]
futebol['total'] = sum(partidas)
print('-=' * 30)
print(futebol)
print('-=' * 30)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {futebol["nome"]} jogou {len(futebol["gols"])} partidas.')
for i, v in enumerate(futebol['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {futebol["total"]} gols.')
