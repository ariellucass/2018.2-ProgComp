texto = input('Informe algo: ')

texto_invertido = ''
qt_letras = 0
posicao = 0

# Obtendo a quantidade de caracteres
for letra in texto: 
  qt_letras += 1

# Montando o texto invertido
while posicao < qt_letras:
   texto_invertido = texto[posicao] + texto_invertido
   posicao += 1

print(' ')
print('O Valor Informado: {0}'.format(texto))
print('O Valor Invertido: {0}'.format(texto_invertido))
print(' ')

#Verificando se são Palíndromos
if (texto == texto_invertido):
   print('São Palíndromos')
else:
   print('Não são Palíndromos')