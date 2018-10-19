import random

lista_B = []
lista_I = []
lista_N = []
lista_G = []
lista_O = []

for contador in range(1, 6):
   # Gerando um número inteiro aleatório entre 1 e 15
   numero_B = random.randint(1,15)
   # Adicionando o número gerado na lista se ele não já estiver nela
   if numero_B not in lista_B: lista_B.append(numero_B)
   numero_I = random.randint(16,30)
   # Adicionando o número gerado na lista se ele não já estiver nela
   if numero_I not in lista_I: lista_I.append(numero_I)
   # Gerando um número inteiro aleatório entre 31 e 45
   numero_N = random.randint(31,45)
   # Adicionando o número gerado na lista se ele não já estiver nela
   if numero_N not in lista_N: lista_N.append(numero_N)
   # Gerando um número inteiro aleatório entre 46 e 60
   numero_G = random.randint(46,60)
   # Adicionando o número gerado na lista se ele não já estiver nela
   if numero_G not in lista_G: lista_G.append(numero_G)
   # Gerando um número inteiro aleatório entre 61 e 75
   numero_O = random.randint(61,75)
   # Adicionando o número gerado na lista se ele não já estiver nela
   if numero_O not in lista_O: lista_O.append(numero_O)


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

