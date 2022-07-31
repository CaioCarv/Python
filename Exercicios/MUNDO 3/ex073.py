times = ('Cruzeiro', 'Vasco', 'Bahia', 'Grêmio', 'Tombense', 'Londrina', 'Sport', 'Sampaio', 'Criciúma', 'CRB')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os quatro últimos colocados são: {times[5:10]}')
print(f'Times em ordem alfabética: {sorted(times)}')
for pos, time in enumerate(times[0:1]):
    print(f'O {time} está na {pos +1}° posição')