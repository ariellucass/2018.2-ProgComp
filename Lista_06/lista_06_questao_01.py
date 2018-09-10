valor = int(input("Entre com um valor, digite 0 para encerrar o programa"))

maior = 0

while (valor != 0) :
    valor = int(input("Entre com um valor, digite 0 para encerrar o programa"))
    if (valor > maior):
      maior = valor

print("O maior valor digitado foi {0}" .format(maior))