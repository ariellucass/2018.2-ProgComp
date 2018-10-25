import random

n = int(input('Informe o Valor de N: '))

# Lista que irá armazenar todos os valores gerados randômicamente
lista = []

quartil_1 = 0
quartil_2 = 0
quartil_3 = 0
quartil_4 = 0

# Gerando a lista randômicamente
for contador_1 in range (0,n):
   lista.append(random.randint(0,99))

# Verificando em que quartil o valor está
for x in lista:
   if x >= 0 and x <= 24:
      quartil_1 += 1
   elif x >= 25 and x <= 49:
      quartil_2 += 1
   elif x >= 50 and x <= 74:
      quartil_3 += 1
   else:
      quartil_4 += 1

# Imprimindo os valores
print('')
print(lista)
print('')
print('No 1º Quartil (0 - 24) foram gerados {0} números'.format(quartil_1))
print('')
print('No 2º Quartil (25 - 49) foram gerados {0} números'.format(quartil_2))
print('')
print('No 3º Quartil (50 - 74) foram gerados {0} números'.format(quartil_3))
print('')
print('No 4º Quartil (75 - 99) foram gerados {0} números'.format(quartil_4))
print('')
