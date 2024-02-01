def SumSquareN(n):
    if n == 1:
        return 1
    return n*n+SumSquareN(n-1)


print(SumSquareN(5))