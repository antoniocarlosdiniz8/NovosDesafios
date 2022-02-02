pares = []
impares = []
full = []
while True:
    full.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar: S/N')).upper().strip()[0]
    if 'N' in resp:
        break
for i, v in enumerate(full):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Minha lista completa: {full}')
print(f'Minha lista de pares: {pares}')
print(f'Minha lista de impares: {impares}')

