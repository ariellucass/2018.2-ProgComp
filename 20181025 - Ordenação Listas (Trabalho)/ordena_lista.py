import random
import os
import datetime

# Chamando o comando CLEAR para limpar o conteúdo da tela
os.system('clear')


# Quantidade de elementos da lista
n = 10000


# Lista que irá armazenar todos os valores gerados randômicamente
listaValores = []


# Gerando a lista randômicamente
print('')
print('------------------------------------------------------------------')
print('Gerando a Lista Randômicamente:')
for x in range (0,n):
   listaValores.append(random.randint(0,1000))


# Salvando a lista gerada em arquivo
arquivo = open('listaoriginal.txt','w')
for valor in listaValores:
   arquivo.write('{0}\n'.format(valor))
arquivo.close()

# Ordenando a lista
print('')
print('------------------------------------------------------------------')
print('Ordenando a Lista Gerada: ')
print('')
horaInicial = datetime.datetime.now()
print('Ordenação Iniciada às...: {0}'.format(horaInicial))


qt_iteracoes = 0
#------------------------------------------------------------------------
# Início do algoritmo de ordenação


# Final do algoritmo de ordenação
#------------------------------------------------------------------------

print('')
horaFinal= datetime.datetime.now()
print('Ordenação Finalizada às.: {0}'.format(horaFinal))
print('')
tempoGasto = horaFinal - horaInicial
print('Tempo de Ordenação......: {0}'.format(tempoGasto))
print('')
print('Quantidade de Iterações.: {0}'.format(qt_iteracoes))
print('------------------------------------------------------------------')


# Salvando a lista ordenada em arquivo
arquivo = open('listaordenada.txt','w')
for valor in listaValores:
   arquivo.write('{0}\n'.format(valor))
arquivo.close()
