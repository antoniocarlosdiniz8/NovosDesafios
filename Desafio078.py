'''maior e menor valor com posições'''
valores = []
maior = menor = 0
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição: {p}:  ')))
    if p == 0:
        maior = menor = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        if valores[p] < menor:
            menor = valores[p]

print(f'{valores}')
print(f'O maior valor da lista é: {maior}, e está nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...')
print(f'O menor valor da lista é: {menor}, e está nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...')