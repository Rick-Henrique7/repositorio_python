lista1 = [] # inicialmente criando duas listas
lista2 = []
armazena1 = int(input('digite numeros para a primeira lista e 0 para sair'))
# enquanto a entrada for diferente de 0 sera apendado na lista
while armazena1 != 0:
    lista1.append(armazena1)
    armazena1 = int(input('0 para sair'))
armazena2 = int(input('digite os numeros para asegunda lista e 0 para sair '))
while armazena2 != 0:
    lista2.append(armazena2)
    armazena2 = int(input('0 para sair '))
lista1.extend(lista2)  # extend usado para colocar uma lista dentro daa outra
print(f'O resultado é igual á {lista1}')