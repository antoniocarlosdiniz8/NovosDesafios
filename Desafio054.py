from datetime import date

anoatual = date.today().year

contnovo = 0
contvelho = 0

for p in range(1, 8):
    anonas = int(input(f'Digite o ano de nascimento da {p}º pessoa: '))
    if anoatual - anonas <= 21:
        contnovo += 1
    else:
        contvelho += 1
print(f'Tivemos {contnovo} menores de idade:')
print(f'E {contvelho} pessoas maiores de idade:')

