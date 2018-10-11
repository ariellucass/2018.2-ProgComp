# Declarando uma lista vazia
listaValores = []

while True:
   # Lendo um valor
   valor = int(input('Informe um valor: '))
   # Adicionando o valor a lista
   listaValores.append(valor)
   # Imprimindo a lista
   print(listaValores)
   # Saindo do laço quando for digitado o valor 0
   if (valor == 0): break

# Eliminando a última posição da lista
print('')
listaValores.pop()
print(listaValores)

# Eliminando a terceira posição da lista
print('')
listaValores.pop(2)
print(listaValores)

# Inserindo um valor em uma determinada posição da lista
print('')
y = int(input('Informe um novo valor: '))
listaValores.insert(2, y)
print(listaValores)

# Exibindo o maior valor da lista
print(max(listaValores))

# Exibindo o menor valor da lista
print(min(listaValores))

# Exibindo a soma dos valores da lista
print(sum(listaValores))
