#Este é o exercício 4 da Lista 1 /Python para Zumbis Prof. Masanori
#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = int(input("Digite o salário atual: "))
porcentagem = int(input("Digite a porcentagem: "))
novo = (salario * (porcentagem / 100)) + salario
print ("Novo salário é: ",novo )
