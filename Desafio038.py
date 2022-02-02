n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

if n1 > n2:
    print(f'O primeiro numero é MAIOR:')
elif n2 > n1:
    print(f'O segundo numero é MAIOR:')
else:
    print('Não existe MAIOR ambos são IGUAIS')
