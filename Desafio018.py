'''Faça um programa que leia um ângulo qualquer, e mostre
seno, cosseno e tangente'''
from math import sin, cos, tan, radians

an = float(input('Digite um angulo?'))

se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))

print(f'Seno: {se:.2f}\n Coseno: {co:.2f}\n Tangente: {ta:.2f}')