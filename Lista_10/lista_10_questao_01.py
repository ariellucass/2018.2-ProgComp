import random

lista = []

try:
   # Informando a quantidade de elementos da lista
   valor_n = int(input('Informe a quantidade N de elementos da lista: '))
except ValueError: # Tratando o erro de valor inválido
   print('O valor N informado não é um inteiro válido...')
else:
   # Preenchendo a lista
   for i in range(0, valor_n):
      lista.append(random.randint(0,valor_n*valor_n))
   try:
      # Informando a posição desejada na lista
      valor_x = int(input('Informe a posição X desejada da lista: '))
   except ValueError: # Tratando o erro de valor inválido
      print('O valor X informado não é um inteiro válido...')
   else:
      try:
         print(lista[valor_x]) # Imprimindo a posição desejada
      except IndexError: # Tratando o erro de posição inválida na lista
         print('A posição X informada está fora da lista...')
finally:
   print('Fim do Programa...')

