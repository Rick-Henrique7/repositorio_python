def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista)-1
    while baixo<=alto:
        meio = (baixo+alto)//2
        chute = lista[meio]
        if chute == item:
            print(f"valor encontrado em indice {meio}")
            break
        elif chute > item:
            alto = meio-1
        else:
            baixo = meio+1
    return print("nao encontrado")

lista = list(range(1,100)) # o ultimo valor é extrinseco

pesquisa_binaria(lista,1)

texto = "eu amo, meu tigrinho, favorito,tigrinho"
print(texto.split(","))