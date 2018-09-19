texto = input('Informe algo: ')

vogais = 'aeiouAEIOUãõÃÕáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛäëïöüÄËÏÖÜ'
consoantes = 'qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNMñÑ'
numeros = '0123456789'

contador_vogais = 0
contador_numeros = 0
contador_consoantes = 0
contador_outros = 0

for letra in texto:
    if (letra in vogais):
      contador_vogais = contador_vogais + 1
    elif (letra in consoantes):
      contador_consoantes = contador_consoantes + 1
    elif (letra in numeros):
      contador_numeros = contador_numeros + 1
    else:
      contador_outros = contador_outros + 1

print('A quantidade de Vogais é {0}'.format(contador_vogais))
print('A quantidade de Consoantes é {0}'.format(contador_consoantes))
print('A quantidade de Números é {0}'.format(contador_numeros))
print('A quantidade de Outros Caracteres é {0}'.format(contador_outros))