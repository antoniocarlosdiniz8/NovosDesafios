n = int(input('Digite um numero: '))
c = n
f = 1
print(f'Calculando {n}! ', end='')
while c > 0:#SEMPRE VAI PRECISAR DO CONTADOR
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c = c - 1#c -= 1
print(f'{f}')
'''n = int(input('Digite um numero: '))
f = 1
print(f'{n}!', end=' ')
for c in range(n, 0, -1):
    f = f * c #f *= c
    print(f'{c}', end=' ')
    print(f'x' if c > 1 else '=', end=' ')
print(f'{f}')'''




