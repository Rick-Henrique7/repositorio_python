string = 'AAACTBF'
string2 = 'CBT'
a = set(string)
b = set(string2)
resultado = a & b
print(resultado)

string3 = 'TTAAC'
c=string3.count('T')
d=string3.count('A')
e=string3.count('C')
print(f' a letra T aparece {c}, a letra A aparece {d}, a letra C aparece {e}')

dicionario = {}
for letra in string3:
    if letra in dicionario:
            dicionario[letra] = dicionario[letra]+1
    else:
        dicionario[letra]=1
print(dicionario)