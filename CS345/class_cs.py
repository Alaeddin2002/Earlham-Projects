

def square_root(x, e):
    """ a function called square_root that estimates the square root of a number using Newton's method.

    ----------
    x : int
     The first parameter will be the number you want to find the square root of.

    e : int
     The next parameter will be the total number of estimates.

    -------
    int
     This function returns the last estimated value.

"""
    s=(x/2)
    for i in range (e-1):
        s = (s + (x/s))/2
    return (s)
square_root(9, 4)

