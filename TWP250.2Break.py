#TWP250Break
#Calcular soma de um númmero inteiro n até ser interrompido

soma = 0

while True:
    n = int(input('Digite o número a somar, ou 0 para sair: '))
    if n == 0:
        break
    soma = soma + n

print('A soma é igual a: ' ,soma)
