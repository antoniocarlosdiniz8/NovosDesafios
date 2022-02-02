'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
 que ele conquistou no final do jogo.'''
from random import randint

total = 0
while True:
    num = int(input('Digite um numero: '))
    palpitepc = randint(0, 10)
    totalip = num + palpitepc

    resp = ' '
    while resp not in 'PpIi':
        resp = str(input('PAR ou ÍMPAR! P/I: ')).strip().upper()[0]
    print(f'Voçê jogou: {num}\nComputador jogou: {palpitepc}')
    print('DEU PAR:' if totalip % 2 == 0 else 'DEU IMPAR:')
    if resp == 'Pp':
        if totalip % 2 == 0:
            print('Voçê venceu!!!')
            total += 1

        else:
            print('Voçê Perdeu!!!')
            break
    if resp == 'Ii':
        if totalip % 2 == 1:
            print('Voçê venceu!!!')
            total += 1
        else:
            print('Voçê Perdeu!!!')
            break
    print('vamos jogar novamente:')
print(f'GAME OVER!!Voçê venceu {total} vezes')

