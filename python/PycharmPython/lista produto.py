produto1 = ["maçã", 10, 0.3]
produto2 = ["laranja", 10, 0.5]
produto3 = ['suco', 2, 10.5]
lista_produto = [produto1, produto2, produto3]

for e in lista_produto:
    print(f'\n produto {e[0]}')
    print(f' quantidade {e[1]} ')
    print(f' preço {e[2]} \n')