#Faça um Programa que leia três números e mostre o maior deles.

a = int(input('Digite o primeiro número.'))
b = int(input('Digite o segundo número.'))
c = int(input('Digite o terceiro número.'))

if a >= b and a >= c:
    print('O número %d é o maior entre os digitados.' %a)
elif b >= c:
    print('O número %d é o maior entre os digitados.' %b)
else:
    print('O número %d é o maior entre os digitados.' %c)
