somaidade = 0
mediaidade = 0
maioridademan = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'-------{c}º PESSOA--------')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite seu SEXO: M/F: '))[:]
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridademan = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridademan:
        maioridademan = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        totmulher20 += 1
mediaidade = somaidade/4

print(f'A média de idade do grupo é: {mediaidade}')
print(f'O mais velho é: {nomevelho} e tem {maioridademan} anos')
print(f'Existem {totmulher20} mulheres com menos de 20 anos')