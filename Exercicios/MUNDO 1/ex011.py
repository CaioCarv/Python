lag = float(input('Qual largura da parede? '))
alt = float(input('Qual altura da parede? '))
area = float(lag * alt)
tint = float(area / 2)
print('Para pintar toda a area, {}M, será necessario {} latas de tinta'.format(area, tint))
