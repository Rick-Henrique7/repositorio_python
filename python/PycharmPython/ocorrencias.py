string = 'um tigres , dois tigres, tres tigres'
p = 0
while p>-1:
    p = string.find('tigre', p)
    if p>=0:
        print(f'posição:{p}')
        p+=1

print(' a contagem de tigres é {}'.format(string.count('tigre')))
# o metodo find retorna um valor corespondente ao indice numerico onde se encontra a string, caso contrario sera devolvido um numero inteiro negativo

