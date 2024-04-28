import random
for e in range(10):
    print(random.uniform(1,10))
    print('\n')#intervalos necessarios em a e b

#tipos de numeros randomicos e seus acessos = radom.random ('cria numeros randomicos entre 0 e um')
#random.randint ('cria numeros aleatorios inteiros') , parametros de começo e fim
#ramdom.uniform (' cria numeros racionais aleatorios') , parametros de começo e fim

for e in range (1,5):# cria numeros randomicos racionais entre 0 e 1
    print(random.random() )

for e in range(10):
    print(random.randint(1,10))# cria numeros aleatorios inteiros entre 1 e 10

print(random.sample(range(1,101),6))# dentro do parametro e sample é criado um espaço amostral no qual a variavel k
# é o numero de elementos nos quais o computador pode escolher
# o espaço amostral pode ser uma lista ja pronta ou pode ser um range sinalizado com ,k pelo elemental


#elmento shuflle utilizado para embaralhar
a = list(range(1,11))
random.shuffle(a)# aqui há um embaralhamento da variavel a pelo shuffle
print(a)