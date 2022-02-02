numeros = []

while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Numero adicionado com sucesso!!')
    else:
        print('Valor Duplicado não vou adicionar:')
    r = str(input('Quer continuar: S/N')).upper().strip()[0]
    if r in 'Nn':
        break
numeros.sort()
print(f'Voçê digitou os valores: {numeros}')
