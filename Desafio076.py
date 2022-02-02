listagem = ('Lápis', 0.50, 'Borracha', 1.00, 'Caneta', 1.50,
            'Apontador', 2.50, 'Régua', 3.00, 'Grampo', 5.00,
            'Postite', 7.00, 'Corretivo', 4.50, 'Perfurador', 3.75)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:.>7.2f}')

#len(listagem) MOSTRA O FINAL DA TUPLA
#listagem[pos] MOSTRA O ITEM QUE ESTÁ EM CADA ÍNDICE DA TUPLA
