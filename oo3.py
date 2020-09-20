from random import randint
from time import sleep
conputador= randint(0, 5)# faz o conputador pesar
jogador=int(input('em que numero eu pesei?'))# o jogador tenta adivinhar
print('processando')
if jogador==conputador:
    print('parabens voce ganhou')
else:
    print('ganhei eu pesei no numero {} e nao {}'.format(conputador,jogador))

