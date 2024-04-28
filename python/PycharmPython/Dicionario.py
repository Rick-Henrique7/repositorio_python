tabela = {"alface":0.45,
          "batata":0.6 ,
          'macarrao': 0.78,
           'cebola': 2.3,
           'carne': 3.5,
          'alho': 4.36,
          'laranja': 2.3
          }
# dicionarios ao enves de indices possuem chaves keys que são indexadas a um valor
#podemos explorar se algo esta no dicionario da seguinte maneira
print("manga" in tabela) # mostra se existe manga na tabela
print('macarrao' in tabela)

#podemos obter uma lista de chaves do dicionario ou valores do dicionario
print(tabela.keys())
print(tabela.values())