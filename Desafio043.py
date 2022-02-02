'''Exercício Python 43: Desenvolva uma lógica
que leia o peso e a altura de uma pessoa, calcule
seu Índice de Massa Corporal (IMC) e mostre seu status,
 de acordo com a tabela abaixo:'''
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
#FORMULA IMC = Peso ÷ (Altura × Altura)
peso = float(input('Digite seu peso kg: '))
altura = float(input('Digite sua Altura :'))

imc = peso/(altura*altura)
imd = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.1f} m. ')

if imc <= 18.5:
    print('VOÇÊ ESTÁ ABAIXO DO PESO!')
elif 18.5 < imc <= 25:
    print('PESO IDEAL!')
elif 25 < imc <= 30:
    print('SOBREPESO!')
elif 30 < imc <= 40:
    print('OBESIDADE!')
else:
    print('\033[31mOBESIDADE MÓRBIDA!\033[m')



