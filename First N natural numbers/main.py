def Nnumber(n):
    if n>0:                                                             
        Nnumber(n-1)
        print(n, end= ' ')


Nnumber(5)
