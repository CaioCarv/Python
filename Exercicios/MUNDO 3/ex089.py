alunos = [[]]
r = 's'
while r != 'N':
    nome = str(input('Nome:')).upper()
    alunos.append(nome)
    nota1 = int(input('Nota 1:'))
    alunos.append(nota1)
    nota2 = int(input('Nota 2:'))
    alunos.append(nota2)
    r = str((input('Deseja continuar? [S/N]'))).upper()
print(alunos)