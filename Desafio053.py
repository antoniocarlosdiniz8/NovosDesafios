'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print('Temos um PALINDROMO!')
else:
    print('Não é um PALIDROMO!')
print(junto, inverso)'''
#REFAZER USANDO FOR
frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
for letra in range(len(junto), 1, -1):
    print(junto[letra], end='')
print(f'{junto}')

