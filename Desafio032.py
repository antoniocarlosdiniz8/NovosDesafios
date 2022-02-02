from datetime import datetime
anoatual = datetime.today().year
n = int(input('Digite um ano qualquer, ou 0 para o ano atual:'))
#print(f'Voçê está no ano de {anoatual}')'''
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f'O ano {n} é BIXESTO')
else:
    print('NÃO É BIXESTO:')
if n == 0:
    if anoatual % 4 == 0 and anoatual % 100 != 0 or anoatual % 400 == 0:
        print(f'Seu Ano atual é BIXESTO')
    else:
        print('NÃO É BIXESTO:')

