# Exercicio 2 Lista 2
#Determine se um ano é bissexto. Verifique no Google como fazer isso...

ano = int(input('Digite o ano: '))

if (ano % 4) == 0:
	if (ano % 100) != 0:
		print('Este é um ano Bissexto. ')
	elif (ano % 400) == 0:
		print('Este é um ano Bissexto. ')
	else:
		print('Este não é um ano Bissexto.')
else:
		print('Este não é um ano Bissexto.')