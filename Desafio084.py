'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
                                     guardando tudo em uma lista. No final, mostre:
                    A) Quantas pessoas foram cadastradas.
                    B) Uma listagem com as pessoas mais pesadas.
                    C) Uma listagem com as pessoas mais leves.'''

temp = []
principal = []
while True:
    temp.append(str(input('Digite um nome:')))
    temp.append(float(input('Digite o peso:')))
    principal.append(temp[:])#AQUI ESTOU CRIANDO UMA CÓPIA DE TEMP E JOGANDO DENTRO DE PRINCIPAL
    temp.clear()#aqui eu preciso limpar a lista a cada volta do loop
    resp = str(input('Quer continuar? S/N')).strip().upper()[0]
    if 'N' in resp:
        break
print(f'Lista: {principal}')
