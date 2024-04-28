#cria uma classe

class cachorro:
    def __init__(self,nome, idade ,tamanho): # usa construtor init e refere cada varaiavel a si mesama
        self.nome = nome
        self.idade = idade
        self.tamanho = tamanho

    def latir(self): # metodo latir criado
        print(f' Ola meu nome é {self.nome} minha idade é {self.idade} minha autura é {self.tamanho} ')
        #aqui no print foi utilizado a variavel da classe para impressão

class rico(cachorro):# class rico herda classe cachorro
    def __init__(self,nome,idade,tamanho,preferencias): # adicionando uma preferencia no codigo
        super().__init__(nome, idade, tamanho,) #super utilizado para herdar variaveis do construtor
        self.preferencias = preferencias


    def latir2(self): # metodo dois utilizado paraa quando o cachorro for rico
        print(f' Ola meu nome é {self.nome} minha idade é {self.idade} minha autura é {self.tamanho} minhas preferencias são '
              f'{self.preferencias}')



#aqui é um exemplo de como utilizar as classes

cachorro1 = cachorro("Bob",6,1.36)
cachorro1.latir()

cachorro2 = rico('asky',10,2.0,'torta de morango')
cachorro2.latir2()