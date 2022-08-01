lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    for n in lista:
         if n in lista:
             print('Valor já adicionado')
       