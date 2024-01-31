# for reverse the odd numbers order in natural no.
def Onumbers(n):
    if n>0:
        if n%2 == 1:
            print(n)
        Onumbers(n-1)

Onumbers(10)