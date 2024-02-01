def EvenNum(n):
    if n == 0:
        return 0
    return (EvenNum(n-1)+(2*n))



print(EvenNum(5))