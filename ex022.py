nome = str(input('Digite o nome completo de uma pessoa: '))
print(f'Seu nome em maiusculo: {nome.upper()}')
print(f'Seu nome em minusculo: {nome.lower()}')
print(f'Seu nome completo tem {len(nome)} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')

