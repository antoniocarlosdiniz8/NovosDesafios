'''Escreva um programa que leia a velocidade atual de um
carro, se ele ultrapassar 80 km mostre uma msg dizendo
que ele foi multado'''

#Valor multa: 7 R$ porcada KM acima do limite de velocidade
vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    multa = (vel - 80) * 7.00
    print(f'Voçê foi multado no valor de {multa:.2f} R$')
else:
    print('Boa Viagem, Dirija com cuidado!!!')
