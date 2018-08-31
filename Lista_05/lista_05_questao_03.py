'''
Verificando se o ano � BISSEXTO
'''

import sys

ano = int(input('Informe o ano: '))

if ano < 1000 or ano > 9999:
  print('Informe um valor entre 1000 e 9999')
  sys.exit()

ano_auxiliar = ano
ano_auxiliar = ano_auxiliar % 1000
ano_auxiliar = ano_auxiliar % 100

if ano % 4 == 0:
  print('O ano {0} � BISSEXTO'.format(ano))
else:
  print('O ano {0} N�O � BISSEXTO'.format(ano))
