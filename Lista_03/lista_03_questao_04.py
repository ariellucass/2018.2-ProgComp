valor_N = input('Informe o número inteiro: ')

valor_N = int(valor_N)

auxiliar = valor_N

centenas = auxiliar // 100  #obtendo o valor das centenas
auxiliar = auxiliar % 100 #extraindo o valor das centenas

dezenas = auxiliar // 10 #obtendo o valor das dezenas
auxiliar = auxiliar % 10 #extraindo o valor das dezenas

unidades = auxiliar #obtendo o valor das unidades

valor_M = str(unidades) + str(dezenas) + str(centenas)

print('Valor N: ', valor_N)

print('Valor M: ', valor_M)
