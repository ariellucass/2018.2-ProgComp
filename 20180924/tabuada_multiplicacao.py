valor_n = int(input('Informe um número entre 1 e 9: '))

if (valor_n) in range(1,11):
   for contador in range (1, 11):
      print('{0} x {1} = {2}'.format(valor_n, contador, valor_n*contador))
else:
   print('Valor Informado Inválido!!!!!')​
