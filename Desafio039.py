from datetime import date

anoatual = date.today().year

anonas = int(input('Digite ano do seu nascimento: '))
idade = anoatual - anonas
if idade == 18:
    print(f'\033[33mVOÇÊ PRECISA SE APRESENTAR ESTE ANO!\033[m')
elif idade < 18:
    saldo = 18 - idade
    print(f'\033[36mAINDA NÃO ESTÁ NO SEU ANO DE ALISTAMENTO!, AINDA FALTA {saldo} anos\033[m')
    print(f'\033[33mSEU ANO DE ALISTAMENTO É EM {saldo+anoatual}\033[m')
elif idade > 18:
    saldo = idade - 18
    print(f'\033[31mVOÇÊ PASSOU DO TEMPO DE SE ALISTAR\nVOÇÊ TERÁ QUE PAGAR UMA MULTA NO VALOR DE R$ 4,50,\nE SE APRESENTAR IMEDIATAMENTE!,\nVC DEVERIA TER SE APRESENTADO HÁ {saldo} anos\033[m')
    print(f'ERA PRA VC TER SE APRESENTADO EM {anoatual-saldo}')


#print(f'Idade {idade} anos')
