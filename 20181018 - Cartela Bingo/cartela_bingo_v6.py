import random

cartela_bingo = []

# Gerando e adicionando os numeros da letra B na lista cartela_bingo
valor_inicial = 1
valor_final   = 15
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(valor_inicial, valor_final)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

cartela_bingo.append(lista)

# Gerando e adicionando os numeros da letra I na lista cartela_bingo
valor_inicial = 16
valor_final   = 30
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(valor_inicial, valor_final)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

cartela_bingo.append(lista)

# Gerando e adicionando os numeros da letra N na lista cartela_bingo
valor_inicial = 31
valor_final   = 45
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(valor_inicial, valor_final)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

cartela_bingo.append(lista)

# Gerando e adicionando os numeros da letra G na lista cartela_bingo
valor_inicial = 46
valor_final   = 60
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(valor_inicial, valor_final)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

cartela_bingo.append(lista)

# Gerando e adicionando os numeros da letra O na lista cartela_bingo
valor_inicial = 61
valor_final   = 75
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(valor_inicial, valor_final)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

cartela_bingo.append(lista)

print(cartela_bingo)
