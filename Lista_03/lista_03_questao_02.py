salario_bruto = input('Informe o salário bruto (R$): ')

salario_bruto = float(salario_bruto)

desconto_previdencia = salario_bruto * 0.1

desconto_imposto = (salario_bruto - desconto_previdencia) * 0.05

salario_liquido = salario_bruto - desconto_previdencia - desconto_imposto

print('Salário Bruto (R$): ', salario_bruto)

print('Desconto Previdência Social (R$): ', desconto_previdencia)

print('Desconto Imposto (R$): ', desconto_imposto)

print('Salário Líquido (R$): ', salario_liquido)

print('Salário Líquido R$ {:.3f}'.format(salario_liquido))