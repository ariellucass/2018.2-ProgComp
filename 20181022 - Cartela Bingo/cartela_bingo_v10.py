import lib_bingo

cartela_bingo = []

# Gerando e adicionando os numeros da letra B na lista cartela_bingo
cartela_bingo.append(lib_bingo.gera_lista(1, 15))

# Gerando e adicionando os numeros da letra I na lista cartela_bingo
cartela_bingo.append(lib_bingo.gera_lista(16, 30))

# Gerando e adicionando os numeros da letra N na lista cartela_bingo
cartela_bingo.append(lib_bingo.gera_lista(31, 45))

# Gerando e adicionando os numeros da letra G na lista cartela_bingo
cartela_bingo.append(lib_bingo.gera_lista(46, 60))

# Gerando e adicionando os numeros da letra O na lista cartela_bingo
cartela_bingo.append(lib_bingo.gera_lista(61, 75))

print(cartela_bingo)

print('')

# Imprimindo a cartela do bingo
print(lib_bingo.imprime_cartela(cartela_bingo))
