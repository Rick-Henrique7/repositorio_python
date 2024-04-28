l = list(range(10,200,3))# programa que cria indice com numero usando enumerate
for y, x in enumerate(l):
    print(f'indice {y} - numero {x}')

# usando o comando de iteração
lista2 = list(range(1,20,4))
i = iter(lista2)

class OpcaoInvalidaError(Exception):
    pass
while True:
    try:
        proximo = str(input('deseja o proximo elemento "yes" para o proximo e "not" para sair'))
        if proximo == 'yes':
            print(next(i))
        elif proximo == 'not':
            break
        else:
            raise OpcaoInvalidaError('digite um valor "YES" ou "NOT"')
    except ValueError:
        print('vc precisa digitar ou yes ou not')
    except StopIteration:
        print('a lista ja acabou')
    except OpcaoInvalidaError as e:
        print(e)