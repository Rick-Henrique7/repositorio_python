#encontrar o maior e o menor valor de uma lista
Lista = [0,2,3,5,9,12,35,15]
print(Lista)
while True:
    try:
        valor1 = int(input('digite um valor da lista'))
        valor2 = int(input('digite outro numero da lista'))
        if valor1 in Lista and valor2 in Lista:
            break
        else:
            print('um dos dois numeros ou ambos nãp estão na lista')
    except ValueError:
            print('é necessario um numero inteiro que exista na lista')
def maior_minimo(valor1,valor2,Lista):
    maior = valor1 if valor1>valor2 else valor2
    print('o maior valor é : {:-^10}'.format(maior))

valor = int(input('digite um eleemento para ser encontrado'))
def encontrar(Lista, valor):
    for indice, elemento in enumerate(Lista):
        if elemento == valor:
            return print('econtrado na posição {:-^10}'.format(indice))
    return None

maior_minimo(valor1,valor2,Lista)
encontrar(Lista,valor)