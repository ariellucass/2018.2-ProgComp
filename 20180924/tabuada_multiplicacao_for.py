valor_x = 0

#while (valor_x < 1) or (valor_x > 10):
while not valor_x in range(1, 11):
   valor_x = int(input('Informe um número: '))
else: 
   if valor_x in range(1, 11):
      #auxiliar = 1
      #while (auxiliar <= 10):
      for auxiliar in range(1, 11):
         tabuada = valor_x * auxiliar
         print('{0} x {1:2} = {2:2}'.format(valor_x, auxiliar, tabuada))
         #auxiliar += 1

