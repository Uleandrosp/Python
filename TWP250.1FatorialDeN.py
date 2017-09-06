#TWP250Acumuladores
#Calcular fatorial de um númmero inteiro n

cont = 1
fat = 2

n = int(input('Digite o numero fatorial: '))

while cont <= n:
    fat = cont * fat
    cont = cont + 1

print('O fatorial de %d é: %d'%(n,fat))
