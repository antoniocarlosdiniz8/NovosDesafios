#0 - 1 - 1 - 2 - 3 - 5

termo = int(input('Digite quantos termos vc quer? '))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3
while c <= termo:
    print(f'{t1}-{t2}-{t3}', end='')
    c += 1
print(' - Fim')
