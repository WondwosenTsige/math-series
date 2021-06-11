# The following fibonaci function will take one parameter
# The function should return the nth value in fibonaci series

def fibonaci(n):

    """ if n == 0:
        return 0
    if n == 1:
        return 1 """

    if n < 2:
        return n
    else: 
        return fibonaci(n-1) + fibonaci(n-2)

# The following Lucas function will take one parameter
# The function should return the nth value in the Lucas series

def lucas(n):

    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n,x = 0,y = 1):
    
    if x == 0 and y ==1:
        return fibonaci(n)
    if x == 2 and y ==1:
        return lucas(n)


