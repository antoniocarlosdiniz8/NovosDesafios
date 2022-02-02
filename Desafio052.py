num = int(input('Digite um numero:'))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[31m', end=' ')
        cont += 1
    else:
        print(f'\033[32m', end=' ')
    print(f'{c}', end=' ')
if cont == 2:
    print(f'\n\033[mO numero {num} é PRIMO, por que foi divisivel apenas {cont} vezes')
else:
    print(f'O numero {num} não é PRIMO pois foi divisivel {cont} vezes')
