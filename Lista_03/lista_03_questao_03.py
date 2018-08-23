codigo = input('Informe um codigo númerico de 5 digitos: ')
codigo = int(codigo)

digito_A = codigo // 10000 # obtendo o primeiro dígito
codigo = codigo % 10000 # extraindo o primeiro dígito

digito_B = codigo // 1000 # obtendo o segundo digito
codigo = codigo % 1000 # extraindo o segundo digito

digito_C = codigo // 100 # obtendo o terceiro digito
codigo = codigo % 100 # extraindo o terceiro dígito

digito_D = codigo // 10 # obtendo o quarto digito
codigo = codigo % 10 # extraindo o quarto digito

digito_E = codigo #obtendo o quinto digito

soma_digitos = (6*digito_A) + (5*digito_B) + (4*digito_C) + (3*digito_D) + (2*digito_E)

digito_V = soma_digitos % 7

print('O digito verificador é: ', digito_V)
