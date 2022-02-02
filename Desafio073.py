time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atletico-GO')

print('-='*15)
print(f'Lista de times: {time}')
print('-='*15)
print(f'5 primeiros colocados: {time[0:5]}')
print(f'4 últimos colocados: {time[-4:]}')
print(f'{sorted(time)}')
print(f'O Chapecoense está na posição: {time.index("Chapecoense")+1}')