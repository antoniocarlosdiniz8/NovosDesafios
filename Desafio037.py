numero = int(input('Digite um numero:'))

print('Escolha uma das bases para conversão:')
print('[1] Converter para \033[36mBINÁRIO\033[m')
print('[2] Converter para \033[34mOCTAL\033[m')
print('[3] Converter para \033[35mHEXADECIMAL\033[m')
opcao = int(input('Digite sua Opção! '))
if opcao == 1:
    print(f'{numero} convertido para \033[36mBINÁRIO\033[m é: {bin(numero)[2:].upper()}')
elif opcao == 2:
    print(f'{numero} convertido para \033[34mOCTAL\033[m é: {oct(numero)[2:].upper()} ')
elif opcao == 3:
    print(f'{numero} convertido para \033[35mHEXADECIMAL\033[m é: {hex(numero)[2:].upper()} ')
else:
    print(f'\033[31mDIGITE UMA OPÇÃO VÁLIDA\033[m')