#TWP230Acumuladores
#Calcule a média de 10 números inteiros

cont = 1
soma = 0

while cont <= 10:
    numero = int(input('Digite o número %d: ' %cont))
    soma = numero + soma
    cont = cont + 1

print('A média da soma ',soma, 'é: %d' %(soma/10))
