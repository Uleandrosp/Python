#Este é o exercício 6 da Lista 1 /Python para Zumbis Prof. Masanori
#6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer 
#e a velocidade média esperada para a viagem.

distancia = float(input("Digite a distância a percorrer em quilometros: "))
velocidade = float(input("Digite a velocidade média em quilometros: "))
tempo = (distancia / velocidade)
print ('Tempo gasto em Km/h: ', tempo, 'hr')

