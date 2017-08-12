#Este é o exercício 5 da Lista 1 /Python para Zumbis Prof. Masanori
#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.

preco = float (input("Digite o preço da mercadoria: "))
desconto = float (input("Digite o percentual de desconto: "))
desconto = desconto /100 
pagar = preco -(preco * desconto)
print ("O valor do desconto é: ", desconto, " E o preço a pagar: %.2f" %pagar)
