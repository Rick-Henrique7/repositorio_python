palavra = input('digite a palavra secreta').lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ''
    for letra in acertos:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('voce acertou')
        break
    tentativa = input('\nDigite uma letra').lower().strip()
    if tentativa in digitadas:
        print('voce ja tentou essa letra!')
        continue
    else:
        digitadas+=tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('VOCE ACERTOU!')
    print('X==:==\nX  :   ')
    print('X  O  'if erros>=1 else'X')
    linha2 = list('')
    if erros == 2:
        ' | '.join(linha2)
    elif erros == 3:
        ' | '.join(linha2)
    elif erros == 4:
        ' / '.join(linha2)
    print(f'X{linha2}')
    linha3 = list('')
    if erros == 5:
        ' / '.join(linha3)
    elif erros >=6:
        linha3 += ' / \ '
    print(f'X{linha3}')
    print('X\n=========')
    if erros == 6:
        print('Enforcado!')
        break



