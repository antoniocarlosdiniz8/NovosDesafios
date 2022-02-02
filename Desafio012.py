produto = float(input('Digite o preço do produto R$'))

desconto = produto - (produto*5)/100

print(f'Preço antigo: {produto:.2f} R$ \nNovo preço: {desconto:.2f} R$')