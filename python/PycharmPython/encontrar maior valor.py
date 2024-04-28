lista = [0,1,5,9,7,4,10,3,20] # definindo a lista
maximo = lista[0] # definnindo o primeiroo elemento da lista como o maior numero
for i in lista: # para todos os elementos da lista
    if i > maximo: # se o numero contido no indice for maior do que maximo
        maximo = i # o valor maximo vai receber o maior indice
print(maximo)