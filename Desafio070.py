menor = maiormil = totaltudo = cont = 0
barato = ''
while True:
    print('===LOJAS DINIZ===')
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    totaltudo += preco
    if preco > 1000:
        maiormil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar> S/N')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total dos produtos digitados é: R$ {totaltudo:.2f}')
print(f'Temos {maiormil} produtos custando mais que 1000 R$: ')
print(f'O produto mais barato é: {barato} e custa: {menor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))
