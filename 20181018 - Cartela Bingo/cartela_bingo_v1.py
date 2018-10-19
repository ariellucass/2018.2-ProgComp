import random

lista_B = []
lista_I = []
lista_N = []
lista_G = []
lista_O = []

for contador in range(1, 6):
   # Adicionando um numero inteiro aleatório entre 1 e 15 na lista_B
   lista_B.append(random.randint( 1,15))
   # Adicionando um numero inteiro aleatório entre 16 e 30 na lista_I
   lista_I.append(random.randint(16,30))
   # Adicionando um numero inteiro aleatório entre 31 e 45 na lista_N
   lista_N.append(random.randint(31,45))
   # Adicionando um numero inteiro aleatório entre 46 e 60 na lista_G
   lista_G.append(random.randint(46,60))
   # Adicionando um numero inteiro aleatório entre 61 e 75 na lista_O
   lista_O.append(random.randint(61,75))


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

