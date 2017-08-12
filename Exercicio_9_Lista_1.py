#Este é o exercício 9 da Lista 1 /Python para Zumbis Prof. Masanori
#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
#assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float (input('Digite a quantidade de quilometros percorridos: '))
dias = float (input('Digite a quantidade de dias que o carro foi alugado: '))

km_rodado = km * 0.15
dias_usados = dias * 60
pagar = km_rodado + dias_usados

print('O preço a pagar é: R$ %.2f'%pagar)