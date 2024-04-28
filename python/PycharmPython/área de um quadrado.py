try:
    x = int(input('digite o lado do quadrado'))
except ValueError:
    print('é necessário um numero inteiro')

def area_quadrada(x):
    return pow(x,2) # um terceiro termo pode ser utilizado para potencia modular

print(area_quadrada(x))