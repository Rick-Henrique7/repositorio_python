tabuada = 1
while tabuada<=10:
    numero = 1
    while numero<=10:
          print(f'{tabuada} x {numero} = {tabuada*numero}')
          numero+=1
    tabuada+=1
    if tabuada==11:
        tabuada=1
        numero=1
    parada = int(input('para parar digite 1?'))
    if parada ==1:
      break
