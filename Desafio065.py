resp = 's'
maior = menor = cont = media = soma = 0
while resp not in 'Nn':
    n = int(input('Digite um numero? '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    media = soma / cont
    resp = str(input('Dejeja continuar: N/S: ')).strip()[0]
print(f'A media dos valores é? {media:.2f}')
print(f'O maior é: {maior} e o menor é: {menor}')
print('Fim')