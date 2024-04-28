lista = []
armazena = int(input('dgite um numeros para a media aritmetica\n digite 0 para sair'))
while armazena != 0:
    armazena = int(input('\n digite 0 para sair'))
    lista.append(armazena)

media =float (sum(lista))/len(lista)
print(f'a medeia é {media:.2f}')