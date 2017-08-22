# Pergunte a velocidade do carro, com valor inteiro.
# Caso ultrapasse 110 km/h exiba uma mensagem que o usuário foi multado, e o valor da multa.
# Cobrado R$ 5,00 por km acima de 110.

velocidade = int(input('Digite a velocidade do veículo: '))

if velocidade > 110:
    multa = (velocidade - 110)*5
    print('Você foi multado por velocidade acima do permitido. Multa no valor de: R$%.2f' %multa)
if velocidade <= 110:
    print('Velocidade dentro do permitido.')
