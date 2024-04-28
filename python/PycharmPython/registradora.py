soma = 0
while True:
     codigo = int(input('qual o codigo do produto de 1 a 5, ou digite 0 para sair'))
     if codigo==1:
        preço =0.50
     elif codigo==2:
        preço =1.00
     elif codigo==3:
        preço =4.00
     elif codigo ==4:
        preço =7.00
     elif codigo == 5:
        preço =8.00
     if codigo==0:
         break
     quantidade = int(input('qual a quantidade'))
     soma = soma + preço*quantidade
print(soma)