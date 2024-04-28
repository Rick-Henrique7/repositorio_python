#center usado para centralizar uma cadeia de carateres
s = 'O homem roxo'
print("X"+s.upper().center(80,'-')+'X')
#metudo just usado para ajustar
h = ' ele procurou por todos '
print(h.lower().ljust(50,'-'))
print(h.upper().rjust(50,'-'))
#o metodo split é utilizado para separar uma cadeia de caracteres com base em uma string exemplo """
i ='vamos , brincar , brincar , e brincar'
print(i.split(','))

uba= ' um tigre dentro de um tigre dentro de um tigre'
print(uba.lower().replace('tigre', 'gato'))

terror = 'vamos brincar hahahahahahaha'
print(f'{terror:>60}')

print(terror.replace("", '-'))

texto = 'Lar é onde meu gato está; Gatos amam mais as pessoas do que elas permitiriam. Mas eles têm sabedoria suficiente para manter isso em segredo (Mary Wilkins); Uma gato transforma o retorno a uma casa vazia no retorno ao lar; Ao olhar nos olhos de um gato, você vê refletido todo o amor que nenhum ser humano jamais conseguirá te dar (Mayara Benatti);'
print(texto.lower().replace('gato', 'puta'))