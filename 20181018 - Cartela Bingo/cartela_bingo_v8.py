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
   return lista
# --------------------------------------------------------------------------


cartela_bingo = []

# Gerando e adicionando os numeros da letra B na lista cartela_bingo
lista_B       = gera_lista(1, 15)
cartela_bingo.append(lista_B)

# Gerando e adicionando os numeros da letra I na lista cartela_bingo
lista_I       = gera_lista(16, 30)
cartela_bingo.append(lista_I)

# Gerando e adicionando os numeros da letra N na lista cartela_bingo
lista_N       = gera_lista(31, 45)
cartela_bingo.append(lista_N)

# Gerando e adicionando os numeros da letra G na lista cartela_bingo
lista_G       = gera_lista(46, 60)
cartela_bingo.append(lista_G)

# Gerando e adicionando os numeros da letra O na lista cartela_bingo
lista_O       = gera_lista(61, 75)
cartela_bingo.append(lista_O)

print(cartela_bingo)
