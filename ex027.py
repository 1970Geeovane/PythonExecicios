nome = str(input('Digite seu nome completo: ')).strip()
primeiroNome = nome.split()
print(f'Seu primeiro nome é {primeiroNome[0]}')
print(f'Seu ultimo nome é {primeiroNome[len(primeiroNome)-1]}')

