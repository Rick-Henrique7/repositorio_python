n = 1   # programa acumula e conta a soma dos primeiros 5 numeros digitados
soma =0
while n<= 5:
    x = int(input(f"digite o {n} numero "))
    soma = soma + x
    n = n +1
print(" a soma é dos primeiros cinco numeros é igual a {}".format(soma).center(90,'-').upper())
