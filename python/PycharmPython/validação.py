try:
    x = int(input('digite um numero para saber se é par ou impar'))
except ValueError:
    print('é necessario um numero')
def épar(x):
    return x%2==0
def eh_par_ou_impar(x):
    if épar(x):
        return 'é par'
    else:
        return 'é impar'

print(eh_par_ou_impar(x))