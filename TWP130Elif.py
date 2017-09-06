#TWP130 Estruturas aninhadas
#Utilizando os valores do exercicio anterior utilizar elif.

consumo = float(input('Digite a quantidade de minutos utilizados: '))

if consumo < 200:
   valor = consumo * 0.20
elif consumo <= 400:
     valor = consumo * 0.18
elif consumo <= 800:
     valor = consumo * 0.15
else:
     valor = consumo * 0.08

print('Valor da conta:R$%.2f' %valor)
