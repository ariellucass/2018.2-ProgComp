import sys

print('-------------------------------------------')
print('Calculando Raizes de uma Equacao do 2o Grau')
print(' ')

valor_a = float(input('Informe o valor de A: '))
valor_b = float(input('Informe o valor de B: '))
valor_c = float(input('Informe o valor de C: '))

print(' ')

if (valor_a == 0):
   print('Nao e uma equacao do 2o grau')
   sys.exit()

delta = valor_b ** 2 - 4 * valor_a * valor_c

if (delta < 0):
   print('A equacao não possui raiz real')
   sys.exit()

raiz_x1 = (-valor_b + delta ** (1/2)) / (2 * valor_a)

if (delta == 0):
   print('A equacao possui duas raizes reais e iguais (X1 = X2)')
   print('X1 = {0:.2f} e X2 = {0:.2f}'.format(raiz_x1))
else:
   print('A equacao possui duas raizes reais e distintas')
   raiz_x2 = (-valor_b - delta ** (1/2)) / (2 * valor_a)
   print('X1 = {0:.2f} e X2 = {1:.2f}'.format(raiz_x1,raiz_x2))

print(' ')
print('-------------------------------------------')
