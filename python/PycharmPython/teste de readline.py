with open('junto','w') as junto:
    with open('pares','r') as par, open('ímpares','r') as impar:
        for linha_impar, linha_par in zip(impar,par):
            for num_par in linha_par.split():
                junto.write(num_par+',')
            for num_impar in linha_impar.split():
                junto.write(num_impar+',')

with open('pares','r') as pares:
    with open('venv/Lib/textos/decremental', 'w') as decremento:
        linhas = pares.readlines()
        ultima_linha = len(linhas)
        decremento.write(ultima_linha)

