class veiculo:
    def __init__(self,nome,velocidade, kilometros_litro):
        self.nome = nome
        self.velocidade = velocidade
        self.kilometros_litro=kilometros_litro

    def ToStr(self):
        print(f'nome {self.nome}')
        print(f'velocidade maxima {self.velocidade}')
        print(f'kilometragem por litro = {self.kilometros_litro}\n')

    def capacidade_assentos(self,capacidade):
        print(f'a capacidade de assentos é igual a {capacidade:_^10}\n')#TODO: preciso aprender mais sobre classes

class Onibus(veiculo):
    def capacidade_assentos(self, capacidade=70):
        return super().capacidade_assentos(capacidade=70)

onibus_escolar = Onibus("scania",120,8)
onibus_escolar.ToStr()
onibus_escolar.capacidade_assentos()

modelo_carro=veiculo('Fusca',200,2)
modelo_carro.ToStr()