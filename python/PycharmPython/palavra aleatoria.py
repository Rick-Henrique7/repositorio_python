n_aleatoria = []
palavra = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F'}
import random
for e in range(0,6):
    n_aleatoria.append(random.randint(1,6))
for elemento in n_aleatoria:
    print(palavra[elemento])
