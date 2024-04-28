compras = []
while True:
    produto = input('qual o produto:')
    if produto == 'fim':
        break
    quantidade = input('qual a quantidade:')
    valor = input('qual o valor')
    compras.append([produto, quantidade,valor])
soma = 0.0
for e in compras:
    print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1]*e[2]:6.2f}")
    soma+= e[1] * e[2]
print(f'total ={soma:.2f}')



