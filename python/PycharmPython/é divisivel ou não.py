try:
    x = int(input('primeiro valor'))
    y = int(input('segundo numero'))
except ValueError:
    print('o valor deve ser um numero inteiro')

def eh_multiplo(x,y):
    if x%y==0:
        return True
    else:
        return False
print(eh_multiplo(x,y))