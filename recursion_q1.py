# print n number using recursion

def show(n):
    if ( n == 0):
        return
    print(n)
    show(n-1)
