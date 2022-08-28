from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'CURSOEMVIEO.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho(f'\033[034m     Saindo do sistema... \033[m'),
        sleep(1),
        cabeçalho('\033[1;35m   Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1)

