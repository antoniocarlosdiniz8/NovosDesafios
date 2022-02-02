palavras = 'aprender', 'programar', 'linguagem','python', 'curso', 'gratis', 'estudar','praticar', 'trabalhar', 'mercado', 'pragramador','futuro'

for pos in palavras:
    print(f'\nNa palavra {pos.upper()} temos: ', end='')
    for letra in pos:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')