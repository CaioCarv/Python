pritermo = int(input('Digite o primeiro termo: '))
segtermo = int(input('Digite o segundo termo: '))
cont = 0
for c in range (pritermo, segtermo, 2):
    if (cont < 10):
        print(c)
        cont += 1