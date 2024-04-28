def mdc(a, b): # calcula o mdc utilizando o algoritmo de euclides
    while b:
        a, b = b, a % b
    return a

def mmc(a, b): # calcula o mmc utlizando o mdc
    return abs(a * b) // mdc(a, b) # abs significa valor absoluto ou modulo

def mmc_tres(a, b, c):
    temp_mmc = mmc(a, b) # primeirrramente é feito o mmc entre a e b e dps o resultado é utilizado para fazer novamente o mmc com c
    resultado = mmc(temp_mmc, c)
    return resultado

print(mmc_tres(12, 3, 6))


def fibonacci():
    lista = [0,1]
    novo_numero =0
    n=0
    x=1
    while n < 10:
        novo_numero = lista[x] + lista[x-1]
        lista.append(novo_numero)
        n+=1
    return lista
print(fibonacci())
