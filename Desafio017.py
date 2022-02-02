'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa'''

from math import hypot

catop = float(input('Digite o cateto oposto: '))
catadja = float(input('Digite o cateto adjacente:'))

hipo = hypot(catop, catadja)

print(f'A hipotenusa é: {hipo:.2f}')


