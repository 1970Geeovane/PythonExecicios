from random import choice

nome1 = input('Digite o nome do aluno: ')
nome2 = input('Digite o nome do aluno: ')
nome3 = input('Digite o nome do aluno: ')
nome4 = input('Digite o nome do aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print(f'O escolhido foi; {escolhido}')



