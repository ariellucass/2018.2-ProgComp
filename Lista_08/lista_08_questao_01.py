valor_n = int(input('Informe o Valor de N: '))

#contador = 1
valor_anterior = 0
valor_atual = 1
fibonacci = 1
lista_fibonacci = []

#while (contador <= valor_n):
for contador in range(0, valor_n):
   #print(fibonacci)
   lista_fibonacci.append(fibonacci)
   fibonacci = valor_atual + valor_anterior
   valor_anterior = valor_atual
   valor_atual = fibonacci
   #contador = contador + 1

print('A Sequência de Fibonacci é:')
print(lista_fibonacci)
