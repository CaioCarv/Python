print('\033[1;32;44m-=\033[m' * 10)
print('ANALISADOR DE TRIANGULOS')
print('\033[1;32;44m-=\033[m' * 10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  if r1 == r2 and r1 == r3:
    print('Os segmentos acima PODEM FORMAR triângulo e o triângulo será equilátero!')
  elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Os segmentos acima PODEM FORMAR triângulo e o triângulo será isósceles')
  else:
    print('Os segmentos acima PODEM FORMAR triângulo e o triângulo será escaleno')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

