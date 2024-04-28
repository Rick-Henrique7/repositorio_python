
def imprimir_lista_aninhada(lista, nivel=0):
    for elemento in lista:
        if isinstance(elemento, list):
            imprimir_lista_aninhada(elemento, nivel + 1)
        else:
            # Ajuste a indentação de acordo com o nível
            print("  " * nivel + str(elemento))

# Exemplo de uma lista aninhada
minha_lista = [1, [2, 3, [4, 5,[7,8,[9,10]]], 6], 7, [8, 9]]

# Chame a função para imprimir a lista aninhada com indentação
imprimir_lista_aninhada(minha_lista)
c={}
a='henrique'

print(type(a))
