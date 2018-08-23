raio = input('Informe o raio:')

raio = float(raio)

pi = 3.141516

if raio > 0:
  area = pi * raio ** 2
  print('A área é',area)
else:
  print('Informe RAIO > 0...')
