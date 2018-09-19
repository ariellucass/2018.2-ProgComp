texto = input('Informe algo: ')

contador = 1

for letra in texto:
    if (letra == ' '): contador = contador + 1

print('A quantidade de Palavras é {0}'.format(contador))