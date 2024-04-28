lista = list(range(11))
resultado = []
x = 0
while x < len(lista):
    for num in lista:
        num*=num
        x+=1
    resultado.append(num)
print(num)
print(lista)