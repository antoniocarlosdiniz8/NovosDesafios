a = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(a)}')#Identifica o tipo primitivo
print(f'Só tem espaços? {a.isspace()}')#Verifica se só tem espaços
print(f'É um número? {a.isnumeric()}')#Verifica se é só números
print(f'É alfanumerico? {a.isalnum()}')#Verifica se tem letras e números
print(f'Está em MAIUSCULO? {a.isupper()}')#Verifica se está em MAIUSCULO
print(f'Está em minusculo {a.islower()}')#Verifica se está em MINUSCULO
print(f'Está capitalizada? {a.istitle()}')#Verifica se a primeira letra está CAPITALIZADA