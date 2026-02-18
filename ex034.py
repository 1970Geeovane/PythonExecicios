salario = float(input('Qual o seu salario: '))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
    print(f'Seu salário passou a ser {salario:.2f} reais com aumento de 15%')
else:
    salario = salario + (salario * 10 / 100)
    print(f'Seu salário passou a ser {salario:.2f} reais com aumento de 10%')
