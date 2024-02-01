def OddSum(n):
    if n == 0:
        return 0
    return OddSum(n-1)+2*n-1
    

print(OddSum(10))