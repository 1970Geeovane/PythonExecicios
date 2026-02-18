frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A primeira letra "A" apareceu na posição {frase.find("A")}')
print(f'A ultima posição que ela aparece é {frase.rfind("A")}')
