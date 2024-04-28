palavra = str(input('digite uma palavra'))
tamanho = int(input('digite o tamanho que a palavra deve ter '))

def validacao(palavra, tamanho):
    expecificação = len(palavra)
    if expecificação<tamanho:
       return print('esta dentro do parametro')
    else:
       return print('esta fora de tamanho')
print(validacao(palavra, tamanho))

