dias = int(input('Quantos dias vc quer alugar um carro? '))
km = int(input('Quantos KM vc vai rodar?'))

preco = (dias * 60) + (km * 0.15)

print(f'O valor do seu veiculo é de {preco:.2f} R$')


