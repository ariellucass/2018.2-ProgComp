print('------------------------------------------')

angulo_x = int(input('Informe o ângulo X: '))

angulo_y = int(input('Informe o ângulo Y: '))

angulo_z = int(input('Informe o ângulo Z: '))

soma_angulos = angulo_x + angulo_y + angulo_z

if soma_angulos != 180:
   print('A soma dos ângulos é diferente de 180º')
elif (angulo_x == 0) or (angulo_y == 0) or (angulo_z == 0):
   print('Não pode haver ângulo = 0')
elif (angulo_x < 90) and (angulo_y < 90) and (angulo_z < 90):
   print('O Triângulo é ACUTÂNGULO')
elif (angulo_x == 90) or (angulo_y == 90) or (angulo_z == 90):
   print('O Triângulo é RETÂNGULO')
else:
   print('O Triângulo é OBTUSÂNGULO')

print('------------------------------------------')
 
