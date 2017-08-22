#TWP120 Estruturas aninhadas
#Utilizando os valores do exercicio anterior criar uma promoção para quando utilizar mais que 800min. Tarifa de R$ 0,08.

consumo = float(input('Digite a quantidade de minutos utilizados: '))

if consumo < 200:
    valor = consumo * 0.20
else:
    if consumo <= 400:
        valor = consumo * 0.18
    else:
        if consumo <= 800:
            valor = consumo * 0.15
        else:
            valor = consumo * 0.08

print('Valor da conta:R$%.2f' %valor)
