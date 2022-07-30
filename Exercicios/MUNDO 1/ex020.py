from random import shuffle  
prinome = str(input('Primeiro aluno: '))
segnome = str(input('Segundo aluno: '))
ternome = str(input('Terceito aluno: '))
quanome = str(input('Quarto aluno: '))
lista = [prinome, segnome, ternome, quanome]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será:')
print(lista)