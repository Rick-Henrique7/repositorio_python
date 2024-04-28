lista = []
numero = 0
while True:
    numero = input('digite um numero inteiro: ')
    if numero == 'sair':
        break
    lista.append(numero)
x= 0
p = input('digite um numero para encontrar')
achou = False
while x < len(lista):
    if lista[x] == p:
        achou = True
        break
    x+=1
if achou:
    print(f'{p} encontrado na posição  {lista[x]}')
else:
    print(f'{p} não encontrado')


