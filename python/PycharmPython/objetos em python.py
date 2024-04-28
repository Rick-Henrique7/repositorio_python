def encontarar_minimo(lista_teste):
    minimo = lista_teste[0]
    for elen in lista_teste:
        if elen<minimo:
            minimo = elen
    return minimo

lista_teste = [7,3,8,2,4,7,6]
menor = encontarar_minimo(lista_teste)
print(menor)

#objeto para criar uma avaliação de mnor numero de uma lista 