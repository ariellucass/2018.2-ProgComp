import random
import statistics

n = int(input('Informe o Valor de N: '))

# Lista que irá armazenar todos os valores gerados randômicamente
lista = []

# Gerando a lista randômicamente
for contador_1 in range (0,n):
   lista.append(random.randint(0,99))

# Imprimindo os valores
print('')
print('------------------------------------------------------------------')
print('Lista Gerada.............: ')
print(lista)
print('')
print('Média dos Valores........: {0}'.format(statistics.mean(lista)))
print('')
print('Mediana dos Valores......: {0}'.format(statistics.median(lista)))
print('')
print('Variância dos Valores....: {0}'.format(statistics.variance(lista)))
print('')
print('Desvio Padrão dos Valores: {0}'.format(statistics.stdev(lista)))
print('')
