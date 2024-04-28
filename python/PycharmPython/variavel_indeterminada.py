def usage(caractere='*'): #variavel opcional deve ser utilizada dessa maneira
    return print(caractere*40)
usage('ç')

def retagulo(caractere='-',altura=6,lado=2): # cria um retanguo com parametros opcionais
    linha = caractere *altura
    for i in range(altura):
        print(linha)
retagulo('H',40,30)