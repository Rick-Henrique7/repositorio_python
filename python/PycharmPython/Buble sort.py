L = [5,4,3,2,1] # esse é praticamente o algoritmo interno do buble sort
fim = 5
while fim > 1 : #quando fim for 0 o programa para por que deixa de ser verdade, e isso só acontece quando não a troca de valores
    trocou = False
    x = 0
    while x < (fim-1):
       if L[x] > L[x+1] :
           trocou = True
           temp = L[x]
           L[x] = L[x+1]
           L[x] = temp
       if not trocou:
        break
       fim-=1
for e in L:
    print(e)
#python possui um comando especifico para ordenar uma lista chamadaa sort
