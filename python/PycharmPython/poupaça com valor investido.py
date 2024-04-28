deposito_inicial = float(input('qual o deposito inicial'))
deposito_posterior = float(input('qual o valor investido nos meses posteriores'))
j = float(input('qual a taxa de juros'))
t = 1
while t<= 24:
    montante = deposito_inicial * ((1 + j) ** t)
    if deposito_posterior>0:
        soma = montante+deposito_posterior
        print(soma)
    else:
        print(montante)
    t+=1
