pontos = 0
questão = 1 # questão começando pela primeira, não pode ser alterada e é incrementada
while questão <=3: #maior numero de questões é 3
    resposta = input(f"Resposta da questão {questão}") # pergunta padrão para validação
    if questão == 1 and resposta == "b" or resposta == "B":
        pontos = pontos+1
    if questão == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1
    if questão == 3 and resposta == "c" or resposta == "C":
        pontos = pontos + 1
    questão = questão + 1
print(f" o aluno fez {pontos} pontos(s)")