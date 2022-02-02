'''Faça um programa que leia 3 numeros e mostre
qual o maior e qual o menor'''
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais outro numero:'))
menor = a
if b < a and b < c:
    menor = b
if c<a and c<b:
    menor = c
#Maior
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print(f'Valores digitados: {a}, {b}, {c} ')
print(f'O maior valor é: {maior}')
print(f'O menor é: {menor}')

