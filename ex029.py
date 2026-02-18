velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'MULTADO! Você ultrapassou a velocidade de 80 Km/h')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa será de R${multa:.2f}')
else:
    print(f'PARABENS! Você não ultrapassou a velocidade de 80Km/h, USE O CINTO DE SEGURANÇA!')
