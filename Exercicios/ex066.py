soma = cont =0
while True:
    valor = int(input('Digite um valor [999 para parar]: '))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')