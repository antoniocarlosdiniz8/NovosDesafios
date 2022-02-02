from random import randint
from time import sleep

palpitepc = randint(0, 5)
palpiteux = int(input('Digite um numero entre 0 e 5 que vc acha que o PC pensou:'))

if(palpiteux == palpitepc):
    print('Parabéns vc acertou o palpite do computador:')
else:
    print('OP´S vc errou, TENTE NOVAMENTE!!')
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
sleep(1)
print(f'COMPUTADOR: {palpitepc}')
print(f'SEU PALPITE: {palpiteux}')


