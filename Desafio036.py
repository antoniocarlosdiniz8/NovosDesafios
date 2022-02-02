print(30*'\033[31m=*\033[m')
print('=========\033[34mBEM VINDO AO BANCO MINHA CASA MINHA DIVIDA\033[m=========')
print(30*'\033[32m=*\033[m')
casa = float(input('Qual valor da casa que vc quer financiar?'))
salario = float(input('Qual seu salário?'))
quitar = int(input('Em quantos anos vc pretende quitar essa divida?'))
totmeses = quitar*12
totparcelas = casa/totmeses
desconto = (salario*30)/100
if totparcelas >= desconto:
    print('\033[35mFINANCIAMENTO NEGADO\033[m')
    print('\033[31mSEU SALÁRIO NÃO É SUFICIENTE\033[m')
else:
    print('\033[32mEMPRESTIMO APROVADO!!!\033[m')
print(f'Voçê tem {totmeses} meses para pagar. ')
print(f'valor total da parcela {totparcelas:.2f} R$')
print(f'Valor final total: {totmeses*totparcelas:.2f} R$')
print(f'desconto de: {desconto:.2f}')