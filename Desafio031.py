'''Ask dist travel em KM, 0.50 viagem até 200 km,
0.45 acima de 200 km'''
dist = float(input('Qual distancia é sua viagem em Km?'))
if dist <= 200:
    preco = dist * 0.50
    print(f'Sua viagem vai custar: {preco:.2f} R$')
else:
    preco = dist * 0.45
    print(f'Sua viagem vai dar mais caro: {preco:.2f} R$')
