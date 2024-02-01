def Nsum(n):
    if n == 1:
        return 1
    return Nsum(n-1)+n
    

print("sum is",Nsum(5))