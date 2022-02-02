soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print(f'A soma dos {cont} valores pares é: {soma}')


