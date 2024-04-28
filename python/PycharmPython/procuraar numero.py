try:
    valor = int(input('digite um valor para encontrar'))
except ValueError:
    print('ehnecessario um nuumero inteiro')

def encontrar(lista, valor):
    for x, e in  enumerate(lista):
        if e == valor:
            return x+1
    return None

lista = [20,30,50,60]

print(encontrar(lista,valor))