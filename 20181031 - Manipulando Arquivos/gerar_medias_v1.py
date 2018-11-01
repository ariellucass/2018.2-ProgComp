# Abrindo arquivo em modo de Leitura
arquivo = open('notas_alunos.txt', 'r')

# Armazenando o conteúdo do arquivo na variável

lista_notas =  []
conteudo = arquivo.readline()
lista_notas.append(conteudo[:-1])

while conteudo:
   conteudo = arquivo.readline()
   lista_notas.append(conteudo[:-1])

# Fechando o Arquivo
arquivo.close()

lista_notas.pop()

print(lista_notas)
