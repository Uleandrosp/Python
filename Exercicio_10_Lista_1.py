#Este é o exercício 10 da Lista 1 /Python para Zumbis Prof. Masanori
#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. 
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
#Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros = int(input('Digite quantos cigarros fuma por dia: '))
anos = int(input('Digite quantos anos ja fumou: '))

por_dia =((cigarros * 10) / 1440)
anos_para_dias = ((anos *12)*30)
total = anos_para_dias * por_dia
print ('Dias de vida perdidos: %d dias.'%total)