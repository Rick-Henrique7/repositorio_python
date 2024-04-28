def senha_aleatoria(): # criação de uma função para criaação de senha aleatoria
    import random # biblioteca randomica
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, '&', '*', '$', '@', '#'] # carcteres usados
    senha = [] # armazenamento de senha em uma lista
    for e in caracteres: # para e elementos em caracteres
        senha.append(random.choice(caracteres)) # lista senha vai appendar um numero escolhido em caracteres
        if len(senha) == 5: # se a senha for de tamanho igual a 5 parar em break
            break
    print(senha) # por fim printar a senha por que não seera usada em outro módulo

senha_aleatoria() # chamando a função

def soma(): # that is ok
    x = int(input('digite um numero'))
    y = int(input('digite outro numero'))
    return print(x+y)
# função de soma perguntando dois valores

def fibonacci(x): # criação de uma função para calcular numeros fibonacci até um certo valor desejado
    fibo = [1,1]
    n=1
    while len(fibo)<=x:
        novo = fibo[n]+fibo[n-1]
        n+=1
        fibo.append(novo)
    return print(fibo)
fibonacci(900)

