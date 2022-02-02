'''lado tem que ser meno do que a soma dos
outro 2'''

'''Triângulo Equilátero todos lados iguais
Triângulos Isósceles pelo menos 2 lados igual
Triângulo Escaleno todos lados diferente'''
l1 = float(input('Digite lado 1:'))
l2 = float(input('Digite lado 2:'))
l3 = float(input('Digite lado 3:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esse segmentos \033[31mPODEM FORMAR UM TRIANGULO DO TIPO \033[m')
    if l1 == l2 == l3:
        print(f'\033[32mEQUILÁTERO\033[m')
    elif l1 != l2 != l3 != l1:
        print('\033[33mESCALENO\033[m')
    else:
        print('ISOSCELE')

