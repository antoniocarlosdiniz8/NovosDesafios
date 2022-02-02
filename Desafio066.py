soma = cont = 0
while True:
    n = int(input('Digite um numero: 999 pra PARAR: '))

    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} numeros, é:  {soma}')



