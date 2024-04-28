lista = [[30,'ç'],[40,'r']] # parametros empacotadoss em uma lista
def desenpacota(tamanho=20,caractere='-'): #função com parametros opcionais
    return print(tamanho*caractere) #multplicação de um caracter por um numero variavel
for e in lista: # para os elementos da lista
    desenpacota(*e) #função desempacota por conta do asteristico na frente do elemento

def soma(*lista):
    soma = 0
    for e in lista:
        soma+=e
    return soma

print(soma(2+3+4+5+9+8))