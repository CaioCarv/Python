from modulos import moeda
from modulos import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 25, 5)
