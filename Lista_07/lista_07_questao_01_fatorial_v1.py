valor_n = int(input('Informe o valor de N: '))

fatorial = 1
#contador = 1

#while (contador <= valor_n):
for contador in range(1, valor_n+1):
   fatorial = fatorial * contador
   #contador = contador + 1

print('{0}! = {1}'.format(valor_n,fatorial))
