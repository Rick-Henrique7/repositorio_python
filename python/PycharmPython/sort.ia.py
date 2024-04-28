# Definir uma função para ordenar uma lista
def selection_sort(lista):
  # Percorrer todos os elementos da lista
  for i in range(len(lista)):
    # Encontrar o menor elemento na lista não ordenada
    min_idx = i
    for j in range(i+1, len(lista)):
      if lista[j] < lista[min_idx]:
        min_idx = j
    # Trocar o menor elemento com o primeiro elemento da lista não ordenada
    lista[i], lista[min_idx] = lista[min_idx], lista[i]
  # Retornar a lista ordenada
  return lista

# Exemplo de uso da função
lista = [5, 3, 8, 2, 9, 1]
print("Lista original:", lista)
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)
