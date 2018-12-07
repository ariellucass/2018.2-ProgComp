import os

os.system('clear')

frutas = []

while True:
   nome_fruta = input('Informe o nome da fruta (para sair digite EXIT): ')
   if nome_fruta.upper() == 'EXIT': break

   try:
      estoque_fruta = int(input('Informe o estoque da fruta: '))
      valor_fruta = float(input('Informe o valor de venda da fruta: '))
   except ValueError:
      print('Um dos valores não é um valor válido!!!!')
   else:
      #lista_aux = []
      #lista_aux.append(nome_fruta)
      #lista_aux.append(estoque_fruta)
      #lista_aux.append(valor_fruta)
      frutas.append([nome_fruta, estoque_fruta, valor_fruta])

print(frutas)
