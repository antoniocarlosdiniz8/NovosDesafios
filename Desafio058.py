'''Exercício Python 58: Melhore o jogo do DESAFIO 28
 onde o computador vai “pensar” em um número entre 0 e 10.
  Só que agora o jogador vai tentar adivinhar até acertar,
  mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
computador = randint(0, 5)
print('Acabei de pensar em um numero entre 0 & 5: Tente advinhar!!!')
acertou = False
tentativas = 0
while not acertou:
        jogador = int(input('Qual seu paplpite:'))
        tentativas += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Mais...tente mais uma vez.')
            else:
                print('Menos..tente mais uma vez.')
print(f'Voçê jogou: {jogador}')
print(f'Computador jogou: {computador}')
print(f'Voçê acertou depois de {tentativas} tentativas')

