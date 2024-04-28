try:
    x = int(input('digite um numero inteiro'))
    y = int(input('digite outro numero inteiro'))
except ValueError:
    print('voce precisa de um numero inteiro')

def qual_o_maior(x,y):
    maior = x
    if y>x :
        maior = y
    return maior

print(f' o maior numero é {qual_o_maior(x, y)}')