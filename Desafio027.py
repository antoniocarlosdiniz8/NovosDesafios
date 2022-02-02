'''Faça um programa
que leia o nome completo
de uma pessoa
e mostre o primeiro e último nome da pessoa'''
nome = str(input('Digite seu nome completo: ')).strip().upper()

divide = nome.split()

print(f'Seu primeiro nome é: {divide[0]}')
print(f'Seu ultimo nome é: {divide[len(divide)-1]}')
print(f'Ultimo {len(divide)-1}')
