km = float(input('Quantos kms foi percorrido? '))
dias = int(input('Quantos dias o carro foi alugado? '))
total = (km * 0.15) + (dias * 60)
print(f'O total percorrido foi de {km} kms e {dias} dias, o total a pagar é; R$ {total:.2f} ')