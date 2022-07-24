from random import choice
aluno1 = str(input('O nome de um aluno será: '))
aluno2 = str(input('O nome de um aluno será: '))
aluno3 = str(input('O nome de um aluno será: '))
aluno4 = str(input('O nome de um aluno será: '))
lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = (choice(lista))
print('E o sorteado é o aluno {}, meus parabéns'.format(sorteado))

