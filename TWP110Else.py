#TWP110 Else
# A empresa de telefonia Tchau. Cobra abaixo de 200min. R$0,20/min.
# Entre 200 e 400min. é R$0,18/min. Acima de 400min. é R$0,15/min. Mostrar valor

consumo = float(input('Digite a quantidade de minutos utilizados: '))

if consumo < 200:
    valor = consumo * 0.20
if consumo >= 200 and consumo <= 400:
    valor = consumo * 0.18
else:
    valor = consumo * 0.15

print ("Valor da conta R$%.2f " %valor)
