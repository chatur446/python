# factourial of n using recursion

def calc_fact(n):
    if(n == 1 or n == 0 ):
        return 1
    return calc_fact(n-1)*n


print(calc_fact(7))
