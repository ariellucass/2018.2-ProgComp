print('------------------------------------------')

lado_a = int(input('Informe o lado A: '))

lado_b = int(input('Informe o lado B: '))

lado_c = int(input('Informe o lado C: '))

if (lado_a <= 0) or (lado_b <= 0) or (lado_c <= 0):
   print('Não pode haver LADO IGUAL ou INFERIOR a ZERO')
elif (lado_a >= lado_b + lado_c) or (lado_b >= lado_a + lado_c) or (lado_c >= lado_a + lado_b):
   print('Os lados informados NÃO formam um triângulo')
elif (lado_a == lado_b) and (lado_b == lado_c):
   print('O Triângulo é EQUILÁTERO')
elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
   print('O Triângulo é ISÓSCELES')
else:
   print('O Triângulo é ESCALENO')

print('------------------------------------------')
 
