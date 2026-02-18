distancia = float(input('Quantos km terá a viagem?  '))
preco = distancia * 0.50
if distancia > 200:
    valor = distancia * 0.45
    print(f'O valor da passagem será de R${valor:.2f}')
else:
    print(f'O valor da passagem será de R${preco:.2f}')
