import sys

frutas = { 'laranja':[10, 1.50], 'manga':[30, 2.25], 'abacaxi':[25, 1.25], 'melancia':[15, 3.45]}

nome_fruta = input('informe a fruta: ').lower()

#for x in range(0, len(frutas)):
#   if frutas[x][0] == nome_fruta:
#      estoque_fruta = frutas[x][1]
#      valor_venda   = frutas[x][2]
#      break

try:
   estoque_fruta = frutas[nome_fruta][0]
   valor_venda = frutas[nome_fruta][1]
except KeyError:
   print('A Fruta não existe no dicionário!!!!')
except:
   print('Erro Inesperado: {0}'.format(sys.exc_info()[0]))
else:
   print('O estoque da fruta {0} é {1} e o preço de venda é {2}'.format(nome_fruta,estoque_fruta, valor_venda)) 
finally:
   print('FIM DO PROGRAMA')

