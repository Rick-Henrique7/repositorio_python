with open('venv/Lib/textos/binary', 'r') as arquivo:
    for linha in arquivo.readline():
        print(linha)
import sys
print(f'numero de parametros : {len(sys.argv)}')
for n , p in enumerate(sys.argv):
    print(f'{n} = {p}')