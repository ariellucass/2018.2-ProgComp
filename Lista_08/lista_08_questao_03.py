lista = []

while True:
   valor = int(input('Informe um valor: '))
   if (valor == 0): break
   lista.append(valor)
   if (len(lista)>5): lista.pop(0)
   print(lista)

print('Fim do Programa!!!!')
