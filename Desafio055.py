menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}º pessoa: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O mais pesado é: {maior} KG')
print(f'O menor é: {menor} KG')