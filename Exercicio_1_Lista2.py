# Exercicio 1 Lista 2
#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('Digite o lado A do triângulo: '))
b = int(input('Digite o lado B do triângulo: '))
c = int(input('Digite o lado C do triângulo: '))

if a != b and b != c:
	print('Este é um triângulo Escaleno.')
elif a == b and b == c:
	print('Este é um triângulo Equilátero.')
else:
	print('Este é um triângolo Isóceles.')