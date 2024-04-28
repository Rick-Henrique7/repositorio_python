x= 0
y= 0
while x <= 10: # tabuada contagem dentro de contagem com retorno
    while y <= 10:
        resultado = x * y
        print(f'{x}*{y}={resultado}')
        y+=1
    x+=1
    y=0
    print('\n')