arquivo = open("binary.txt","w") # na primeira instacia cria o arquivo "binary" em seguida é selecionada a opção de leitura "w"
for linha in range(1,101): # para cad alinha em um range de 1 a 101
    arquivo.write(f"{linha}\n") #escrever dentro da variavel, com write o numero da linha e em seguida pular para a linha de baixo
arquivo.close() #arquivo fechado para não consumir recursos do pc