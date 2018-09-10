valor_n = int(input('Informe o Valor de N: '))

contador = 1
valor_anterior = 0
valor_atual = 1

while (contador <= valor_n):
   fibonacci = valor_anterior + valor_atual
   print(fibonacci)
   valor_atual = valor_anterior
   valor_anterior = fibonacci
   contador = contador + 1