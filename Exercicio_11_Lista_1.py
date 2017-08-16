#Este é o exercício 11 da Lista 1 /Python para Zumbis Prof. Masanori
#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

valor = 2 ** 1000000
resp = str(valor)
resp = len (resp)
print ('Quantidade de digitos: ', resp)