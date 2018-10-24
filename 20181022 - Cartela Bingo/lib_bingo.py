import random

# --------------------------------------------------------------------------
# Função para gerar uma lista com 5 números inteiros aleatórios 
# dentro de um intervalo especificado
def gera_lista(intValorInicial, intValorFinal):
   lista    = []
   contador = 0
   while contador < 5:
      numero = random.randint(intValorInicial, intValorFinal)
      if numero not in lista:
         lista.append(numero)
         contador += 1
   lista.sort()
   return lista
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Função para imprimir uma lista no formato de uma cartela de bingo
def imprime_cartela(listaValores):
   linha_cartela =                 '+----+----+----+----+----+\n'
   linha_cartela = linha_cartela + '| B  | I  | N  | G  | O  |\n'
   linha_cartela = linha_cartela + '+----+----+----+----+----+\n'

   # Implementar a impressão das linhas da lista
   
   linha_cartela = linha_cartela + '+----+----+----+----+----+'

   return linha_cartela
# --------------------------------------------------------------------------



