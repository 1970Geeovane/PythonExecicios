from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print(f'Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(f'Parabens! Vocẽ conseguiu me vencer! ')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não {jogador}')
