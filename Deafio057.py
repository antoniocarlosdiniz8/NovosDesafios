'''Faça um programa que digite o sexo de uma pessoa
Mas só aceita M ou F, caso esteja errado peça a digitação
novamente, até ter um valor correto.'''
sexo = str(input('Digite seu sexo M/F: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('DADOS INVÁLIDO, por favor informe seu sexo: F/M: ')).upper().strip()[0]
print(f'Seu sexo é: {sexo}')
