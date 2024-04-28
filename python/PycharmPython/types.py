L = ['a',['b','c',['d','e',['f','g']]]]
def recursiva(L,nivel=0):
    for e in L:
        if isinstance(e,str):
            print('-'*nivel,e)
            nivel+=1
        else:
            for z in e:
                print('-'*nivel,z)
                nivel+=1

recursiva(L)