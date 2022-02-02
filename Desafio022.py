'''Crie um progra que leia
um nome de uma pessoa e mostre:'''
#O nome com todas as letras MAIUSCULA
#O nome com todas as letras minuscula
#Quantas letras ao todo sem contar espaços
#Quantas letras tem o primeira nome
nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print(40*'=')
print(f'Seu nome em MAIUSCULA é: {nome.upper()}')
print(f'Seu nome é Minusculas é: {nome.lower()}')
print(f'Se nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem: {len(separa[0])} letras')
print(40*'=')