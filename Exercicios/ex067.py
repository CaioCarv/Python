n = result = tabuada = 0
while tabuada >= 0:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada >= 0:
        for n in range(1, 10):
            result = tabuada * n
            print(f'{tabuada:.1f} X {n:.1f} = {result}')
print(f'Processo finalizado, obrigado por jogar!')
