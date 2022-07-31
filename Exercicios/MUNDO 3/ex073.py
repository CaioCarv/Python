times = ('Cruzeiro', 'Vasco', 'Bahia', 'Grêmio',
         'Tombense', 'Londrina', 'Sport',
         'Sampaio', 'Criciúma', 'CRB')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=-'*15)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*15)
print(f'O Cruzeiro está na {times.index("Cruzeiro")+1}° posição')