texto = input('Informe algo: ')

texto_invertido = ''

# Montando o texto invertido
for letra in texto:
    texto_invertido = letra + texto_invertido

print(' ')
print('O Valor Informado: {0}'.format(texto))
print('O Valor Invertido: {0}'.format(texto_invertido))
print(' ')

#Verificando se são Palíndromos
if (texto == texto_invertido):
   print('São Palíndromos')
else:
   print('Não são Palíndromos')