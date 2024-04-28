def eh_par(n):
    r = n%2==0
    return r
def soma_pares(lst):
    soma = 0
    for num in lst:
        if(eh_par(num)):
            soma += num
    return soma
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,4,15,16,17,18]
soma = soma_pares(lista)
print(f'o total da soma dos pares da lista é igual a {soma}')
