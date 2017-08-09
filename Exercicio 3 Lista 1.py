#Exercicio 3 da Lista 1 / Python para Zumbis Prof. Masanori

hora = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
hora = (hora * 60) * 60
minutos = minutos * 60
segundos = hora + minutos + segundos
print ("Foram usados: %d segundos" %segundos)
