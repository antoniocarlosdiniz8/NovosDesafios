n = s = c = 0
n = int(input('Digite um numero: 999 pra PARAR!'))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um numero: 999 pra PARAR!'))
print(f'A soma dos numeros é: {s}')
print(f'Voçê digitou {c} numeros: ')

