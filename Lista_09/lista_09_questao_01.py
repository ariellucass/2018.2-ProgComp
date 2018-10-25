import random

n = int(input('Informe o Valor de N: '))

# Lista que irá armazenar todos os valores gerados randômicamente
lista_1 = []

# Lista que irá armazenar apenas 1 valor de cada valor gerado randômicamente
lista_2 = []

# Lista que irá armazenar a quantidade de ocorrências de cada valor gerado
lista_3 = []

for contador_1 in range (0,n):
   # Gerando a lista_1 randomicamente
   x = random.randint(0,9)
   lista_1.append(x)
   # Se o valor gerado não existir na lista_2 ele será adicionado a ela
   if x not in lista_2: lista_2.append(x)


# Verificando a quantidade de ocorrências do valor gerado e
# armazenando em lista_3
for contador_1 in lista_2:
   cont_valor = 0
   for contador_2 in lista_1:
      if contador_1 == contador_2: cont_valor += 1
   lista_3.append(cont_valor)

# Imprimindo os valores
print('')
print(lista_1)
print('')
print(lista_2)
print('')
print(lista_3)
print('')
