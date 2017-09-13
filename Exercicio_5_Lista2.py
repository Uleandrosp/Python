# Faça um Programa que leia três números e mostre o maior e o menor deles.

maior = 0
menor = 0

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a > b and a > c:
    maior = a
    if b < c:
        menor = b
    else:
        menor = c

if b > a and b > c:
    maior = b
    if a < c:
        menor = a
    else:
        menor = c
        

if c > a and c > b:
    maior = c
    if a < b:
        menor = a
    else:
        menor = b
        
print('O menor número é: %d, e o maior é: %d' %(menor,  maior))
