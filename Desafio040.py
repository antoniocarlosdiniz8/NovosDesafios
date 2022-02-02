'''MEDIA 2 NOTAS
5.0 REPROVADO
5.0 E 6.9 RECUPERAÇÃO
>= 7.0 APROVADO'''
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2)/2

print(f'A média entre {n1} e {n2} é {media:.1f}')

if media <= 5.0:
    print(f'\033[31mALUNO REPROVADO!\033[m')
elif 5.0 <= media <= 7.0:
    print(f'\033[33mALUNO DE RECUPERAÇÃO!')
else:
    print(f'\033[32mALUNO APROVADO, PARABÉNS!!!\033[m')

