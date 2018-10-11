# Declarando uma lista vazia
listaValores = []

# Preenchendo a lista
while True:
   # Lendo um valor
   valor = int(input('Informe um valor: '))
   # Adicionando o valor a lista
   listaValores.append(valor)
   # Imprimindo a lista
   print(listaValores)
   # Saindo do laço quando for digitado o valor 0
   if (valor == 0): break

#----------------------------------------
maximo = listaValores[0]
minimo = listaValores[0]
soma   = listaValores[0]

for posicao in range(1, len(listaValores)):
   if (listaValores[posicao] > maximo): maximo = listaValores[posicao]
   if (listaValores[posicao] < minimo): minimo = listaValores[posicao]
   soma = soma + listaValores[posicao]

print(maximo)
print(minimo)
print(soma)





