senha = '123mudar'

texto_entrada = input('Digite a senha: ')

if (texto_entrada.lower() == senha.lower()):
   print('Usuário Autorizado!!!!')
else:
   print('Senha Errada!!!!')
