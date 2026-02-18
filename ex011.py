largura = float(input('Qual a largura da parede? m²'))
altura = float(input('Qual a altura da parede? m²'))
area = largura * altura
quantidade = area / 2
print(f'Area da parede: {area:.2f}m²')
print(f'Precisará de {quantidade:.2f}Ltr. de tinta.')
