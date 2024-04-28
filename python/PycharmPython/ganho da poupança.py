deposito_inicial = float(input('qual o deposito inicial'))
j = float(input('qual a taxa de juros'))
t = 1
while t<= 24:
    montante = deposito_inicial * ((1 + j) ** t)
    print(montante)
    t+=1

