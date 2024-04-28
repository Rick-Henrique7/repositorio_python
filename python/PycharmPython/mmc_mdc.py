def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

resultado_mmc = mmc(8, 9)
print(resultado_mmc)
