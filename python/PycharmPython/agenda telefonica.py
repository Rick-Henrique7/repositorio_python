agenda = [] # variavel agenda é uma lista

def pede_nome():
    return input('Nome: ') # vai receber um input

def pede_telefone():
    return input('Digite seu telefone: ') #pede input do numero de telefone

def mostra_dados(nome, telefone):
    print(f'Nome: {nome} Telefone: {telefone}') # mostra dados do nome e do telefone

def pede_nome_arquivo():
    return input('Nome do arquivo: ') #pede o nome do aruivo

def pesquisa(nome): # peaquisa o nome de uma pessoa na agenda
    nome = nome.lower()
    for p, e in enumerate(agenda): #
        if e[0].lower() == nome:
            return p
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print('Nome não encontrado.')

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado:')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print('Nome não encontrado')

def lista():
    print('\nAgenda\n\n------')
    for e in agenda:
        mostra_dados(e[0], e[1])
        print('------\n')

def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            agenda = []
            for l in arquivo.readlines():
                nome, telefone = l.strip().split('#')
                agenda.append([nome, telefone])
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
            else:
                print(f'Valor fora da faixa permitida. Digite um número entre {inicio} e {fim}.')
        except ValueError:
            print(f'Valor inválido. Favor digitar um número inteiro.')

def menu():
    print('''
    1- Novo
    2- Altera
    3- Apaga
    4- Lista
    5- Grava
    6- Le
    0- Sai''')
    return valida_faixa_inteiro('Escolha uma opção: ', 0, 6)

while True:
    opcao = menu()
    if opcao == 0:
        break
    if opcao == 1:
        novo()
    if opcao == 2:
        altera()
    if opcao == 3:
        apaga()
    if opcao == 4:
        lista()
    if opcao == 5:
        grava()
    if opcao == 6:
        le()
