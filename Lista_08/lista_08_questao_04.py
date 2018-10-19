lista = [None, None, None, None, None]

print(lista)

while True:
   valor = int(input('Informe um valor: '))
   if (valor == 0): break
   lista.append(valor)
   lista.pop(0)
   print(lista)

print('Fim do Programa!!!')

