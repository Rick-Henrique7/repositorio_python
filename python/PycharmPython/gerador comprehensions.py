# objetos geradores são demarcados por ()
#EXEMPLO

y = (x for x in range(100) if x % 3 == 0) # y se torna um gerador compressivo
for i in y: #aqui para cada elemento da lista do gerador ele vai printar o elemento i
    print(i)
print('acabou')


gerator = [(y,x) for (x,y) in [(2,3),(5,9),(12,47)]] # gerador compressivo que retorna uma troca de elementos de uma tupla dentro de uma lista seja ela parametrizada ou nao
print(gerator)

def oloco():
    i=0
    while True:
        yield i
        i+=1

g = oloco()
