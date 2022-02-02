'''Crie uma tupla que escreva por extenso, pedindo um numero entre 0 e 20 do usuário'''
#Escreva apemas o numero digitado por extenso
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete'
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre Zero e Vinte!'))
    if 0 <= num <= 20:
        break
    print('Tente Novamente!!', end='')
print(f'Voçê digitou o numero {numeros[num]}')