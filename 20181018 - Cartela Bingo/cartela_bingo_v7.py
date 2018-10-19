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
valor_inicial = 1
valor_final   = 15
lista_B       = gera_lista(valor_inicial, valor_final)
cartela_bingo.append(lista_B)

# Gerando e adicionando os numeros da letra I na lista cartela_bingo
valor_inicial = 16
valor_final   = 30
lista_I       = gera_lista(valor_inicial, valor_final)
cartela_bingo.append(lista_I)

# Gerando e adicionando os numeros da letra N na lista cartela_bingo
valor_inicial = 31
valor_final   = 45
lista_N       = gera_lista(valor_inicial, valor_final)
cartela_bingo.append(lista_N)

# Gerando e adicionando os numeros da letra G na lista cartela_bingo
valor_inicial = 46
valor_final   = 60
lista_G       = gera_lista(valor_inicial, valor_final)
cartela_bingo.append(lista_G)

# Gerando e adicionando os numeros da letra O na lista cartela_bingo
valor_inicial = 61
valor_final   = 75
lista_O       = gera_lista(valor_inicial, valor_final)
cartela_bingo.append(lista_O)

print(cartela_bingo)
