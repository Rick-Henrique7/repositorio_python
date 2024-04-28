lista = []
while True:
    n = int(input('digite o valor a ser somado e 0 para sair'))
    if n ==0 :
        break
    lista.append(n)
media = (sum(lista))/len(lista)
print("-"*54)

print('voce digitou' ,len(lista) , 'numeros e a media é',media)