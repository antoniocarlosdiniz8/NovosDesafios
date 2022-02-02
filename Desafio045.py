from time import sleep
from random import randint

print('''Escolha uma opção:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
item = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
jogador = int(input('Digite sua opção: '))
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('VC GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('OPÇÃO INVÁLIDA:')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('VC GANHOU')
    else:
        print('OPÇÃO INVÁLIDA:')
elif computador == 2:
    if jogador == 0:
        print('VC GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('OPÇÃO INVÁLIDA:')



print(f'VOÇÊ JOGOU: \033[32m{item[jogador]}\033[m')
print(f'COMPUTADOR JOGOU: \033[34m{item[computador]}\033[m')

