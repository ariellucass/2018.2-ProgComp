'''
programa para verificar se o n�mero
digitado � PAR, �MPAR ou NULO
'''

valor = int(input('Informe o valor: '))

if valor == 0:
   print('O Valor � NULO')
elif valor % 2 == 0 and valor > 0:
   print('O Valor Digitado � PAR POSITIVO')
elif valor % 2 == 0 and valor < 0:
   print('O Valor Digitado � PAR NEGATIVO')
elif valor % 2 != 0 and valor > 0:
   print('O Valor Digitado � �MPAR POSITIVO')
else:
   print('O Valor Digitado � �MPAR NEGATIVO')
