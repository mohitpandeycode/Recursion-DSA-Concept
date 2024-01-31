def Onumbers(n):
    if n>0:
        Onumbers(n-1)
        if n%2 == 0:
            print(n)

Onumbers(10)