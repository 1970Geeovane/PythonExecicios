preço = float(input('Digite o valor do produto:R$ '))
desconto = preço * 5 / 100
print(f'O produto de R${preço:.2f} com desconto de 5%, fica R${preço - desconto:.2f}')
