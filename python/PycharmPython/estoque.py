estoque = {
    'tomate': [1000,2.30],
    'alface': [500,0.45],
    'batata':[2001,1.20],
    'feijão':[100,1.50]
}
venda = []
while True:
    produto = input('digite um produto, e sair para sair')
    if produto == 'sair':
        break
    quantidade = int(input(' digite a quantidade a comprar'))
    if produto in estoque:
        if quantidade < estoque[produto][0]:
            venda.append([produto, int(quantidade)])
        else:
            print(f'quantidade maior doq o estoque, a quantidade no estoque é de {estoque[produto][0]}')
    else:
        print('produto não encontrado')
total = 0
print('vendas:\n')
for operacao in venda:
    produto,quantidade = operacao
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}')
    total+=custo
print(f'o valor total é: {total:3.2f}')
for chave, dados in estoque.items(): #primeira variavel se refere a chave e a segunda a uma tupla do estoque d valores
    print(f' a chave é \n', chave)
    print(f' o valor da tupla é\n',dados)
    print(f'a quatidade é \n', dados[0])
    print(f'o preço é',dados[1])

