print(40*'=')
print('========ANALIZADOR DE TRIANGULO=========')
print(40*'=')

r1 = float(input('Digite a reta 01:'))
r2 = float(input('Digite a reta 02:'))
r3 = float(input('Digite a reta 03:'))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('As retas acima podem formar TRIANGULO!')
else:
    print('As retas acima não podem formar TRIANGULO!')