n = 0
with open('venv/Lib/textos/juntar', 'w') as junto:
    with open('ímpares','r') as impar:
        with open('pares','r') as par:
            n =0
            while n< len(par):
                for elemento in par:
                    junto.write(elemento)
                    for elemento1 in par:
                        junto.write(elemento1)

