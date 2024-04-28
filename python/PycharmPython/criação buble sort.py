lista = [3,3,1,5,4] #lista com quatro elementos
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim-1):
        if lista[x]> lista[x+1]:
            trocou =True
            temp = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temp
        x+=1
    if not trocou:
        break
    fim-=1
for e in lista:
    print(e)
