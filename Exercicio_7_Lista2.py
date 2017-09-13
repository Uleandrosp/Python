''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas. '''

print('Loja de tintas. Versão 1.0')
print('')
area = int(input('Quantos metros quadrados tem a área a ser pintada: '))

if area % 54 == 0:
    latas = area  / 54
else:
    latas = int(area  / 54) + 1

preco = float(latas * 80)

print('O numero de latas a serem comprados é: %d, e o valor será: %.2f'%(latas, preco))