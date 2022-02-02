'''Leia o ano de nasc. de um atleta e mostre na tela sua categoria
de competição.
até 9 anos mirin
até 14 anos infantil
até 19 anos junior
ate 25 anos senior
acima disso master'''
from datetime import date

anoatual = date.today().year

anonas = int(input('Digite o ano de seu nascimento:'))

idade = anoatual - anonas

if idade <= 9:
    print(f'\033[33mO ATLETA TEM {idade} ANOS, CATEGORIA MIRIM!\033[m')
elif 9 < idade <= 14:
    print(f'\033[34mO ATLETA TEM {idade} ANOS, CATEGORIA INFANTIL!\033[m')
elif 14 < idade <= 19:
    print(f'\033[35mO ATLETA TEM {idade} ANOS, CATEGORIA JUNIOR!\033[m')
elif 19 < idade <= 25:
    print(f'\033[36mO ATLETA TEM {idade} ANOS, CATEGORIA SENIOR!\033[m')
else:
    print(f'\033[97mO ATLETA TEM {idade} ANOS, CATEGORIA MASTER!\033[m')

