lista = list(range (0,20,3))
lista2 =list(range(0,30,2))
print(f'{lista}\n {lista2}')
a = set(lista)
b = set(lista2)
print(a & b)

validação = input('digite seu nome ')
a = validação.count('e')
print(f' seu nome possui {a} e')

find = input('digite uma frase')
print(find.find('j', 7, 10)) # o comando find retorna onde esta a posição de uma str em relação a outra string
# para pesquisar porem da esquerda para a direita é utilizado o metodo rfind
print(find.rfind('j'))
# tambem é possivel passar paraametros para o metodo find
