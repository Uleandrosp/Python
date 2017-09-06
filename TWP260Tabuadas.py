#TWP260 Tabuada
#Exibir a tabuada de 1 ao 10

tabuada = 1

while tabuada <=10:
    print('tabuada do %d: ' %tabuada)
    valor = 0
    i = 1
    while i <=10:
        valor = tabuada * i
        print('%d x %d = %d'%(tabuada, i, valor))
        i = i + 1
    tabuada = tabuada + 1
