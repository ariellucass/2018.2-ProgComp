'''
Programa para verificar se os n�meros
digitados s�o m�ltiplos
'''

valor_x = int(input('Informe o Valor X: '))
valor_y = int(input('Informe o Valor Y: '))

if valor_x > valor_y:
  if valor_x % valor_y == 0:
    print('Os N�meros {0} e {1} s�o m�ltiplos'.format(valor_x, valor_y))
  else:
    print('Os N�meros {0} e {1} N�O s�o m�ltiplos'.format(valor_x, valor_y))
else:
  if valor_y % valor_x == 0:
    print('Os N�meros {0} e {1} s�o m�ltiplos'.format(valor_x, valor_y))
  else:
    print('Os N�meros {0} e {1} N�O s�o m�ltiplos'.format(valor_x, valor_y))
