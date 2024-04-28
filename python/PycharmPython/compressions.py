import random #importa a biblioteca aleatoria

L = [c for c in range(10)] # retorne x para os elementos de x num range de 10
print(L)


U =[]
for p in range(100): # apenda numeros do construtor fora da lista vazia
    U.append(p)
print(U)

lista_aleatoria = [random.randint(1,9) for e in range(20)] # numero aleatorio de um a nove para os elementos de e no range de 20
print(lista_aleatoria)

# a sintaxe funciona assim:
# nova = [expressao for variavel in sequencia]

# criação de tupla de para ordenado para uma função

ubuntu = [(i,i*2) for i in range(1,10)]
print(ubuntu)

# pares usando compressão
lista_pares = [x for x in range(10) if x %2 == 0]
print(lista_pares)

# usando a parametrização do range
lista1 = [r for r in range(0,10,2)]
print(lista1)

#sem usar compressão
z = list(range(0,10,2))
print(z)