lista = [1,2,3,4,5,6,7,8]
p = int(input('digite um numero para encontrar'))
x= 0
achou = False
while lista[x] < len(lista):
    if lista[x] == p:
        achou = True
        break
    x+=1
if achou:
    print(f'{p} encontrado na posição {lista[x]}')
else:
    print(f'{p} não encontrado')
