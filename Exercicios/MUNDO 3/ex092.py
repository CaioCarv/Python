from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
carteira = int(input('Número da sua carteira (0 Não tem): '))
if carteira >= 1:
    pessoa['cartTrab'] = carteira
    pessoa['contrato'] = int(input('Em que ano você foi contratado? '))
    contratacao = datetime.now().year - pessoa['contrato']
    pessoa['salario'] = float(input('Qual foi o seu sálario? '))
    anoApos = 35 - contratacao
    aposentar = pessoa['idade'] + anoApos
    print(f'O {pessoa["nome"]} vai se aposentar com {aposentar} anos')
    print(pessoa)
print('-' * 10, 'FIM', '-' * 10)