result = 1
for i in range(1,5):
	result *= i # result = result * i
	print(result)
	
"""
1*1=1
1*2=2
2*3=6
6*4=24

"""

def fiblist(n):
    """ produziert die Liste der Fibbo-Zahlen 
        bis zur n-ten Generation """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]] 
"""
index: -4-3-2-1
Liste:  a, b, c, d
index  0 1  2  3

> [0,1]    + [1](denn: 0+1) = [0,1,1] 
> [0,1,1] + [2](denn: 1+1) = [0,1,1,2]
...

"""
        print(fib)
        return fib

print(fiblist(7))

l1 = [0,1]
l2 = [1]
l3 = [0]

print(l2+l3) # = [1,0]
print(l1[-1]+l1[-2]) # = 1