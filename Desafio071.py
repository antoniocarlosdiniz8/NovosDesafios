print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = float(input('Quanto vc quer sacar: '))
total = saque
ced = 50
totcedula = 0
#nota1 = nota2 = nota5 = nota10 = nota20 = nota50 = nota100 = nota200 = 0
while True:
    if total >= ced:
        total -= ced
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totcedula = 0
        if total == 0:
            break

