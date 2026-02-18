from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2f}')
cos = cos(radians(angulo))
print(f'O angulo de {angulo} tem o cos de {cos}')
tan = tan(radians(angulo))
print(f'O angulo de {angulo} tem o tan de {tan:.2f}')

