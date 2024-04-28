a = lambda x,y: x*y # a variavel  recebe uma função suprimida chamada lambda com parametros x e y
print(a(2,3))


def soma(*lista): #a função soma recebe argumentos empacotados
    soma = 0
    for e in lista:
        soma+=e
    return soma
print(soma(2,3,5,6,4,8)) #soma empacotada em uma tupla soma(x,c,v,b,n,)