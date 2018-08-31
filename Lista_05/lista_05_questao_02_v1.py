'''
Programa para verificar se os números
digitados são múltiplos
'''

valor_x = int(input('Informe o Valor X: '))
valor_y = int(input('Informe o Valor Y: '))

if valor_x > valor_y:
  if valor_x % valor_y == 0:
    print('Os Números {0} e {1} são múltiplos'.format(valor_x, valor_y))
  else:
    print('Os Números {0} e {1} NÃO são múltiplos'.format(valor_x, valor_y))
else:
  if valor_y % valor_x == 0:
    print('Os Números {0} e {1} são múltiplos'.format(valor_x, valor_y))
  else:
    print('Os Números {0} e {1} NÃO são múltiplos'.format(valor_x, valor_y))
