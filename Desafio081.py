lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar?')).strip()[0]
    if resp in 'Nn':
        break
print(f'Voçê digitou {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista!!!')
else:
    print('O valor 5 NÃO está na lista:')
