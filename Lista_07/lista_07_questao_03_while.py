texto = input('Informe algo: ')

contador = 1
qt_letras = 0
posicao = 0

# Obtendo a quantidade de caracteres
for letra in texto: 
  qt_letras += 1

while posicao < qt_letras:
    if (texto[posicao] == ' '): contador += 1
    posicao += 1

print('A quantidade de Palavras é {0}'.format(contador))