lista_primos = [2]

for contador in range(3, 101, 2):
   print('Verificando se {0} é primo...'.format(contador))
   divisor = False
   for contador2 in lista_primos:
      if (contador % contador2 == 0):
         divisor = True
         break
   if not divisor:
      lista_primos.append(contador)

print(lista_primos)
