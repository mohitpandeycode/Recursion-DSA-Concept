# for reverse the first 10 odd numbers in natural no.
def Onumbers(n):
    if n>0:
        print(2*n-1)
        Onumbers(n-1)

Onumbers(10)