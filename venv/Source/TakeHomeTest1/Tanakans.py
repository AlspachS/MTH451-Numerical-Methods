import math

def test1(x):
    return (math.e**-x) + math.cos(x)

def test2(x):
    return (10*x*(math.e**(-x**2))) - 1

def test3(x):
    return x**3 - 2*x + 2

def test4(x):
    return x**2 - math.e**x - 3*x + 2

def test5(x):
    return math.sin(x) - (x/2)

def test6(x):
    return math.sin(x) - x**5 + x**3 - 1

def test7(x):
    return x**4 + 7*x**3 + 6*x**2 - 28*x - 40

def dtest7(x):
    return 4*x**3 + 21*x**2 + 12*x - 28

def ModifiedBisectionAlgorithm(a, b, f, tol=0.1e-7):
    if(f(a) * f(b)) > 0:
        raise("No zero in this interval.")

    counter = 0
    while(True):
        left = None
        c = (a + b) / 2
        a, b, left = (a, c, False) if f(a)*f(c) < 0 else (c, b, True)

        m = (f(b) - f(a)) / (b - a)
        c = (f(a) - m*a) if left else (f(b) - m*b)
        x = -c/m

        if abs(f(x)) < tol:
            return counter, x

        counter += 1
        a, b = (a, x) if f(a)*f(x) < 0 else (x, b)

def NewtonsMethod(a, f, df, tol=0.1e-7, maxIter=100):
    i = 0
    while abs(f(a)) > tol and i < maxIter:
        i += 1
        a = a - f(a)/df(a)

    return(i, a)

def BisectionMethod(a, b, f, tol=0.1e-7):
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
        mid = (a + b) / 2
        midEvaled = f(mid)
        if midEvaled * bEvaled > 0:  # f(mid) > 0
            b = mid
        elif midEvaled * aEvaled > 0:  # f(mid) < 0
            a = mid
        else:
            return (mid, True)
        return (a, b)

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

    return (count, a)

# print(ModifiedBisectionAlgorithm(-2, 2, test1))
# print(ModifiedBisectionAlgorithm(-1, 1, test2))
# print(ModifiedBisectionAlgorithm(-3, 3, test3))
# print(ModifiedBisectionAlgorithm(-2, 2, test4))
# print(ModifiedBisectionAlgorithm(-3, 5, test5))
# print(ModifiedBisectionAlgorithm(-5, 2, test6))

print("Algorithm\tInterval\tIterations\tSolution")

iterations, solution = ModifiedBisectionAlgorithm(0, 3, test7, 10e-6)
print("MBA\t\t\t[0, 3]\t\t{0}\t\t\t{1}".format(iterations, solution))

iterations, solution = BisectionMethod(0, 3, test7, 10e-6)
print("Bisection\t[0, 3]\t\t{0}\t\t\t{1}".format(iterations, solution))

iterations, solution = NewtonsMethod(0, test7, dtest7, 10e-6)
print("Newton's\ta=0\t\t\t{0}\t\t\t{1}".format(iterations, solution))

iterations, solution = NewtonsMethod(3, test7, dtest7, 10e-6)
print("Newton's\ta=3\t\t\t{0}\t\t\t{1}".format(iterations, solution))

