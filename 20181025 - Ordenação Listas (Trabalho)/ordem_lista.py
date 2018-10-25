from random import * 
from os import *


# --------------------------------------------------------------------------
# Função para gerar uma lista com 5 números inteiros aleatórios 
# dentro de um intervalo especificado
def ordena_lista(lstLista):
   lstLista_Ord = lstLista
	#Implementar o algoritmo de ordenação
   return lstLista_Ord
# --------------------------------------------------------------------------


# Chamando o comando CLEAR para limpar o conteúdo da tela
system('clear')

# Quantidade de elementos da lista
n = 10000

# Lista que irá armazenar todos os valores gerados randômicamente
listaValores = []

# Gerando a lista randômicamente
arquivo_lista_original = open('lista_original.txt', 'w')
print('')
print('------------------------------------------------------------------')
print('Gerando a Lista Randômicamente:')
for x in range (0,n):
   listaValores.append(randint(0,1000))
arquivo_lista_original.write(listaValores)
arquivo_lista_original.close()

# Ordenando a lista
print('')
print('------------------------------------------------------------------')
print('Ordenação Iniciada às: ')
print('')
print('Ordenando a Lista Gerada:')

arquivo_lista_ordenada = open('lista_ordenada.txt', 'w')
listaValores_ord = ordena_lista(listaValores)
arquivo_lista_ordenada.write(listaValores_ord)
arquivo_lista_ordenada.close()

print('')
print('Ordenação Finalizada às: ')
print('')
print('Tempo de Ordenação: ')
print('')
print('------------------------------------------------------------------')