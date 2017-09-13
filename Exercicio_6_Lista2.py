# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido, conforme a tabela abaixo:
#   a. + Salário Bruto : R$
#   b. - IR (11%) : R$
#   c. - INSS (8%) : R$
#   d. - Sindicato ( 5%) : R$
#   e. = Salário Liquido : R$

valor = float(input('Digite o Valor da hora: '))
hora = float(input('Digite a quantidade de horas trabalhadas: '))

salario = valor * hora
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
liquido = salario - ir - inss - sindicato
print('')
print('O salário do mês foi: R$%.2f' %salario)
print('O Imposto de Renda do mês foi: -R$%.2f' %ir)
print('O INSS do mês foi: -R$%.2f' %inss)
print('O desconto de Sindicato do mês foi: -R$%.2f' %sindicato)
print('O Salário Liquido do mês foi: =R$%.2f' %liquido)
