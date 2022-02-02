'''Exercício Python 44: Elabore um programa que calcule
 o valor a ser pago por um produto, considerando o seu preço
  normal e condição de pagamento:'''
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
produto = float(input('Digite o valor do seu produto: '))
print(40*'=')
print('=======QUAL A FORMA DE PAGAMENTO?=======')
print('1 - \033[33mÁ VISTA/CHEQUE: 10% DE DESCONTO\033[m')
print('2 - \033[34mÁ VISTA NO CARTÃO: 5% DE DESCONTO\033[m')
print('3 - \033[35m2X NO CARTÃO: PREÇO NORMAL\033[m')
print('4 - \033[36m3X OU MAIS NO CARTÃO: 20% DE JUROS\033[m')
print(40*'=')
opcao = int(input('ESCOLHA A FORMA DE PAGAMENTO DE ACORDO COM A TABELA ACIMA: '))


if opcao == 1:
    desconto = produto - (produto * 10)/100#CALCULA O DESCONTO DE 10% DO VALOR DO PRODUTO
    print(f'Seu produto que era {produto} R$\nagora com desconto vc vai pagar: {desconto} R$')
elif opcao == 2:
    desconto = produto - (produto * 5)/100#CALCULA O DESCONTO DE 5% DO VALOR DO PRODUTO
    print(f'Seu produto que custava {produto:.2f} R$\nagora com desconto vc vai pagar: {desconto:.2f} R$')
elif opcao == 3:
    desconto = produto / 2
    print(f'Seu produto no valor de {produto:.2f} ficou 2 x de {desconto:.2f} R$')
elif opcao == 4:
    vezes = int(input('De quantas vezes vc quer parcelar?'))
    #if vezes >= 3:
    valorfinal = produto + (produto * 20)/100
    print(f'Seu produto que custava {produto:.2f} R$\nAgora vai custar {valorfinal:.2f} R$ com JUROS\nem {vezes} x de {valorfinal/vezes:.2f} R$')
else:
    print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!')



