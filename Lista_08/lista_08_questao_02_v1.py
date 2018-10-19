lista_primos = [2]

for contador in range(3, 101, 2):
   print('Verificando se {0} é primo...'.format(contador))
   divisores = False
   for contador2 in range(0, len(lista_primos)):
      if (contador % lista_primos[contador2] == 0):
         divisores = True
         break
   if not divisores:
      lista_primos.append(contador)

print(lista_primos)
