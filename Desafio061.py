print('Gerador de PA:')
print('-='*10)
primeiro = int(input('Digite primeiro termo: '))
razao = int(input('Digite a razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}-', end='')
    termo += razao
    cont += 1
print('FIM')


