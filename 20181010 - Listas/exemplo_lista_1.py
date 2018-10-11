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
