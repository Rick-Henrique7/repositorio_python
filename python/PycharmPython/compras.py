compras = {}  #compras completo
total = 0

while True:
    produto = str(input('qual o nome do produto ou "sair" para sair: '))
    if produto.lower() == 'sair':
        break
    quantidade = int(input('digite a quantidade a ser comprada: '))
    preço = float(input('digite o preço dop produto: '))
    soma = quantidade*preço # a cada iteração do loop essa variavel sera modificada
    compras[produto] = [quantidade, preço, soma]
    total += soma
print('\n')
for produto, info in compras.items(): # podemos criar um gerador de items para toos os elementos do dicionario
    print(f'{produto} a quantidade foi de {info[0]} o preço é {info[1]} e o total foi {info[2]} ')
    print(f'o total de sua compra foi de {total}')

