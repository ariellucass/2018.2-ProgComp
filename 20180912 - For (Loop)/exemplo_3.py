valor_n = int(input('Informe o Valor de N: '))

#contador = 1
valor_anterior = 0
valor_atual = 1
fibonacci = 1

#while (contador <= valor_n):
for contador in range(1, valor_n+1):
   print(fibonacci)
   fibonacci = valor_atual + valor_anterior
   valor_anterior = valor_atual
   valor_atual = fibonacci
#contador = contador + 1
