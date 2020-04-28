def fact1(n):
    if n == 1:
        return 1
    else:
        return n*fact1(n-1)