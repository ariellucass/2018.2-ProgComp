import random

# Gerando e adicionando os numeros da letra B na lista lista_B
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

lista_B = lista

# Gerando e adicionando os numeros da letra I na lista lista_I
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

lista_I = lista

# Gerando e adicionando os numeros da letra N na lista lista_I
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

lista_N = lista

# Gerando e adicionando os numeros da letra G na lista lista_G
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

lista_G = lista

# Gerando e adicionando os numeros da letra O na lista lista_O
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

lista_O = lista

# Imprimindo a lista_B
print(lista_B)
# Imprimindo a lista_I
print(lista_I)
# Imprimindo a lista_N
print(lista_N)
# Imprimindo a lista_G
print(lista_G)
# Imprimindo a lista_O
print(lista_O)

