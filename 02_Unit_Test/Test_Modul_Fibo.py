def fib(n):
    a, b = 0, 1
    for i in range (n):
        a, b = b, a + b
    return a

def fiblist(n):
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]] # Erlärung unter Fibo_List_xmpl.py
    return fib

if __name__ == "__main__":

# Falls Modul in ein anderes Programm importiert wird,
# wurden ohne diesen Ausdruck die folgenden Befehle zusätzlich ausgeführt werden
# Mann will ja nur auf die Funktionen zugreifen

    print (fib(10))
    print (fiblist(10))
