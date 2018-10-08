# --------------------------------------------------------------
# Revisando Strings

texto = input('Informe um texto: ')
print('')

# --------------------------------------------------------------
# Imprimindo o tamanho/comprimento da string (quantidade de caracteres)
tamanho_texto = len(texto)
print('O tamanhho do texto é {0}'.format(tamanho_texto))
print('')

# --------------------------------------------------------------
# Imprimindo a string toda em letras maiúsculas
print(texto.upper())
print('')

# --------------------------------------------------------------
# Imprimindo a string toda em letras minúsculas
print(texto.lower())
print('')

# --------------------------------------------------------------
# Imprimindo o texto de trás pra frente usando FOR
texto_invertido_for = ''
for letra in texto:
    texto_invertido_for = letra + texto_invertido_for
print(texto_invertido_for)
print('')

# --------------------------------------------------------------
# Imprimindo o texto de trás pra frente usando WHILE
contador_letras = 0
texto_invertido_while = ''
while contador_letras < tamanho_texto:
    texto_invertido_while = texto[contador_letras] + texto_invertido_while
    contador_letras += 1
print(texto_invertido_while)

