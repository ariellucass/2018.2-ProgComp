valor = int(input("Entre com um valor, digite 0 para encerrar o programa"))

soma = contador = media = 0

while (valor != 0) :
    soma = soma + valor
    contador = contador + 1
    valor = int(input("Entre com um valor, digite 0 para encerrar o programa"))

if (contador != 0):
   media = soma/contador

print("Você digitou {0} numeros e a média deles foi {1} e a soma {2} " .format(contador, media, soma))
