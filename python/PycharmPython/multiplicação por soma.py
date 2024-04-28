a = int(input("digite um numero:")) # le dois numeros
b = int(input("digite outro numero:"))
print("-"*35)

print(f"{a}*{b} tambem pode ser escrito como:")
print((f"+{a}")*b) #multiplicação por incrementação
print("que é o mesmo que = {}".format(a*b))