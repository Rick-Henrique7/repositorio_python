chave = input('qual a palavra chave')
for x in range(100):
    print()
acertos = 0
tentativas = []
erros = 0

while True:
    letra = input('digite uma letra')
    if letra in tentativas:
        print('voce ja tentou essa letra!')
        continue
    for letras in chave:
        if letra == chave:
            print('Voce acertou a palavra chave!')
            break
        elif letra in chave:
            print('voce acertou')
            tentativas.append(letra)
            acertos +=1
            break
        else:
            print('voce errou')
            erros += 1

