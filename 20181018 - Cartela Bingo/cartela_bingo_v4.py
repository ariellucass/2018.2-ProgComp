import random

# Gerando e adicionando os numeros da letra B na lista lista_B
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(1,15)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

lista_B = lista

# Gerando e adicionando os numeros da letra I na lista lista_I
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(16,30)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

lista_I = lista

# Gerando e adicionando os numeros da letra N na lista lista_N
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(31,45)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

lista_N = lista

# Gerando e adicionando os numeros da letra G na lista lista_G
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(46,60)
   if numero not in lista:
      lista.append(numero)
      contador += 1
# --------------------------------------------------------------------------

lista_G = lista

# Gerando e adicionando os numeros da letra O na lista lista_O
# --------------------------------------------------------------------------
lista    = []
contador = 0
while contador < 5:
   numero = random.randint(61,75)
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

