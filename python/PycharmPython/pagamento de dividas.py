divida_inicial =  float(input('qual a divida inicial'))
juros = float(input('qual a porcentagem de juros'))
pagamento = float(input('qual sera o valor pago mensalmente'))
meses =0

while divida_inicial>0:
    divida_inicial += divida_inicial * (juros/100)
    divida_inicial -= pagamento
    meses +=1

print(f'voce levara {meses} meses para quitar a divida')