lista1 = []
lista2 = []

print('Digite números para a primeira lista e "sair" para encerrar: ')
armazena1 = input()
while armazena1.lower() != 'sair':
    lista1.append(int(armazena1))
    armazena1 = input('Digite outro número (ou "sair" para encerrar): ')

print('Digite números para a segunda lista e "sair" para encerrar: ')
armazena2 = input()
while armazena2.lower() != 'sair':
    lista2.append(int(armazena2))
    armazena2 = input('Digite outro número (ou "sair" para encerrar): ')

# Determina qual lista é maior
maior_lista = lista1 if len(lista1) > len(lista2) else lista2
menor_lista = lista1 if len(lista1) <= len(lista2) else lista2

lista_final = []
for i in range(len(maior_lista)):
    if i < len(menor_lista) and maior_lista[i] != menor_lista[i]:
        lista_final.append(maior_lista[i])
        lista_final.append(menor_lista[i])
    elif i >= len(menor_lista):
        lista_final.append(maior_lista[i])

print(f'A lista final é igual a {lista_final}')
