contmaior = homem = mulhermenor = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M]')).strip().upper()[0]
    if idade >= 18:
        contmaior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1

    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar: [S/N]   ?')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Temos {mulhermenor} mulheres menores que 20 anos:  ')
print(f'Temos {contmaior} pessoas maiores de 18 anos:')
print(f'Foram cadastrados {homem} homens: ')
