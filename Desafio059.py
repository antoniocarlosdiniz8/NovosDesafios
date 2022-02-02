from time import sleep
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''     1 - SOMA
    2 - MULTIPLICAR
    3 - MAIOR
    4 - NOVOS NUMEROS
    5 - SAIR DO PROGRAMA''')
    opcao = int(input('Digite a opção desejada: '))
    sleep(1)
    if opcao == 1:
        print(f'A soma entre {num1} e {num2} é {num1+num2}')

    elif opcao == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif opcao == 3:
        print(f'O maior entre {num1} e {num2} é: {max(num1, num2)}')
        if num1 == num2:
            print('Não existe maior eles são iguais:')
    elif opcao == 4:
        print('Digite novos numeros')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opçãp Inválida...')




