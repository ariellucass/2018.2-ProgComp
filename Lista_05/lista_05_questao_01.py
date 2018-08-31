'''
programa para verificar se o número
digitado é PAR, ÍMPAR ou NULO
'''

valor = int(input('Informe o valor: '))

if valor == 0:
   print('O Valor é NULO')
elif valor % 2 == 0 and valor > 0:
   print('O Valor Digitado é PAR POSITIVO')
elif valor % 2 == 0 and valor < 0:
   print('O Valor Digitado é PAR NEGATIVO')
elif valor % 2 != 0 and valor > 0:
   print('O Valor Digitado é ÍMPAR POSITIVO')
else:
   print('O Valor Digitado é ÍMPAR NEGATIVO')
