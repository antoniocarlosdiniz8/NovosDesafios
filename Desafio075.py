
numeros = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')), int(input('Digite o último numero: ')) )

print(numeros)

if 3 in numeros:
    print(f'O valor 3 foi encontrado na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição:')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'Os valores pares digitados foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(f'\033[36m{c}\033[m', end=' ')

