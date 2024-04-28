
def listsum(numList):
    if len(numList) == 0:
        return 0
    else:
        return numList[0] + listsum(numList[1:])

# Exemplo de uso
print(listsum([1, 3, 5, 7, 9]))  # Saída: 25
