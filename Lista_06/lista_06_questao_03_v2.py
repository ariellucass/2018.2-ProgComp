valor_n = int(input('Informe o valor de N: '))

fatorial = valor_n
contador = valor_n - 1

while (contador > 0):
   fatorial = fatorial * contador
   contador = contador - 1

print('{0}! = {1}'.format(valor_n,fatorial))
