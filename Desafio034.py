sal = float(input('Digite seu salário:'))
acima = 10
abaixo = 15

if sal > 1250:
    aumento = sal + (sal * acima)/100
    print(f'Seu salario era: {sal:.2f} \nAgora passou a ser {aumento:.2f}')
    print(f'teve um aumento de {abaixo}%\n Acrescido de {(sal * acima)/100:.2f} R$')
else:
    aumento = sal + (sal * abaixo)/100
    print(f'Seu salário era {sal:.2f}, agora é: {aumento:.2f}')
    print(f'teve um aumento de  {abaixo}')
