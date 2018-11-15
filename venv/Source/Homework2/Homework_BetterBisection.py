import math

def f(x):
    """
    Test function for verifying the bisetion method works correctly.
    :param x:  Value to evaluate the function at
    :return:
    """
    return math.exp(x) + x - 2

def bisectOnce(a, b):
    """
    One step of the bisection method.  It finds a midpoint between two points,
    determines which half of the interval to discard, then alters the appropriate
    end point to remove that section of the interval.  Returns two values unless
    a zero is found, if a zero is found it returns the value it's at and a boolean
    to indicate to the outer function to stop looping.
    :param a:
    :param b:
    :return:
    """
    aEvaled = f(a)
    bEvaled = f(b)
    mid = (a+b) / 2
    midEvaled = f(mid)
    if midEvaled*bEvaled > 0:       # f(mid) > 0
        b = mid
    elif midEvaled*aEvaled > 0:     # f(mid) < 0
        a = mid
    else:
        return(mid, True)
    return(a, b)

def bisectTolerance(a, b, tol=10e-4):
    """
    Finds a zero of a function by compressing two braketing the zero
    until it finds a value within the given tolerance.  Checks the return type
    of the second variable to see if it's a bool, then breaks the loop
    accordingly.
    :param a:
    :param b:
    :param tol:
    :return:
    """
    if f(a) * f(b) > 0:
        print("Error:  No zero between {} and {}!".format(a, b))
        return

    found = False
    error = abs(b - a) / 2
    count = 0
    while abs(tol) < error and not found:
        a, b = bisectOnce(a, b)
        error = abs(b - a) / 2
        count += 1
        if type(b) == bool:
            found = b

    return(a, b, count)

print(bisectTolerance(0, 5))