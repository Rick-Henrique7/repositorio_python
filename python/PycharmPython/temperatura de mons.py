''' encontrar a menor temperatura registrada e a maior temperatura e ao final exibir uma media '''

temperatura_mons = [ -10 , -8 , 0 , 1, 2 , 5 , -2 , -4]
menor_temp = temperatura_mons[0]
maior_temp = temperatura_mons[0]

for temp in temperatura_mons:
    if temp > maior_temp:
        maior_temp = temp

for temp1 in temperatura_mons:
    if temp1 < menor_temp:
        menor_temp = temp1

media = (sum(temperatura_mons))/len(temperatura_mons)
print(f' a menor temperatura é {menor_temp} e a maior temperatura é {maior_temp} e a media é de {media: .2f}')
