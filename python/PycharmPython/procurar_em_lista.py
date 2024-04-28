palavra = input('Digite: ')
testa = input('Teste de upper "u" ou lower "l": ')

def teste(palavra, testa):
    while True:
        if testa == "u":
            if palavra.isupper(): # a utilizacao de isupper e islower deve conter paranteses exp: islower()
                # a palavra return retorna imediatamente apos  a passagem
                print('Correto')
            else:
                print('Errado')
            break

        elif testa == 'l':
            if palavra.islower():
                print('Correto')
            else:
                print('Errado')
            break

        else:
            print('Opção inválida')
            break

teste(palavra, testa)


