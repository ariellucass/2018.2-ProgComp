import random

lista_B = []
lista_I = []
lista_N = []
lista_G = []
lista_O = []

# Gerando e adicionando os numeros da letra B na lista lista_B
# --------------------------------------------------------------------------
contador = 0
while contador < 5:
   numero_B = random.randint(1,15)
   if numero_B not in lista_B:
      lista_B.append(numero_B)
      contador += 1
# --------------------------------------------------------------------------

# Gerando e adicionando os numeros da letra I na lista lista_I
# --------------------------------------------------------------------------
contador = 0
while contador < 5:
   numero_I = random.randint(16,30)
   if numero_I not in lista_I:
      lista_I.append(numero_I)
      contador += 1
# --------------------------------------------------------------------------

# Gerando e adicionando os numeros da letra N na lista lista_N
# --------------------------------------------------------------------------
contador = 0
while contador < 5:
   numero_N = random.randint(31,45)
   if numero_N not in lista_N:
      lista_N.append(numero_N)
      contador += 1
# --------------------------------------------------------------------------

# Gerando e adicionando os numeros da letra G na lista lista_G
# --------------------------------------------------------------------------
contador = 0
while contador < 5:
   numero_G = random.randint(46,60)
   if numero_G not in lista_G:
      lista_G.append(numero_G)
      contador += 1
# --------------------------------------------------------------------------

# Gerando e adicionando os numeros da letra O na lista lista_O
# --------------------------------------------------------------------------
contador = 0
while contador < 5:
   numero_O = random.randint(61,75)
   if numero_O not in lista_O:
      lista_O.append(numero_O)
      contador += 1
# --------------------------------------------------------------------------

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

