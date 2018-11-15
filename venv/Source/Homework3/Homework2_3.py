# Newton’s Method’s fast convergence relies on the derivative of f being
# non-zero when f is zero. That is, if f(xsub0) = 0 then f`(xsub0) != 0.
# We say such zeros have multiplicity = 1. In general, the multiplicity of a
# zero of f at xsub0 is the lowest number of derivative of f which gives a
# non-zero result at xsub0. So, for example if f(x) = 1−cos(x), then f(0) = 0
# and f`(0) = sin(0) = 0, but f``(0) = cos(0) = 1 != 0. Thus the multiplicity
# of 0 is 2. To ﬁnd higher multiplicity zeros efficiently we must modify
# Newton’s Method so that:

#  xsub(k+1) = xsubk − m * (f(xsubk) / f`(xsubk)) where (m = multiplicity of zero)

# a. Make a copy of newt, call it mnewt, and modify it so that it also takes
# an argument m which is the multiplicity of the zero you’re looking for.
#
# b. Let f(x) = 1−cos(x). Use regular newt and our new program mnewt with
# m = 2 to ﬁnd the zero at x = 0. Compare the number of iterations required.
#
# c. Let f(x) = x**4 − x**3 − 3*x**2 + 5*x − 2. Find the multiplicity of the
# zero of f at x = 1.

# (x**3 - 3*x**2 + 3*x - 1)*(x + 2)
# (x**2 - 2*x + 1) * (x - 1) * (x + 2)
# (x - 1) * (x - 1) * (x - 1) * (x + 2)
# ((x - 1)**3) * (x + 2)
# m at x=1 is 3

# d. Use regular newt and our new program mnewt to ﬁnd the zero of f from the
# previous part at x = 1. Compare the number of iterations required.

import math

def test1(x):
    return 1-math.cos(x)

def dtest1(x):
    return math.sin(x)

def test2(x):
    return x**4 - x**3 - 3*x**2 + 5*x - 2

def dtest2(x):
    return 4*x**3 - 3*x**2 - 6*x + 5

def newtonsMethod(a, f, df, tol=0.001, maxIter=100):
    i = 0
    while abs(f(a)) > tol and i < maxIter:
        i += 1
        a = a - f(a)/df(a)
    return(a, f(a), i)

def newtonsMethodWMultiplicity(a, m, f, df, tol=0.001, maxIter=100):
    i = 0
    while abs(f(a)) > tol and i < maxIter:
        i += 1
        a = a - m * f(a)/df(a)
    return(a, f(a), i)

print(newtonsMethod(3, test1, dtest1))
print(newtonsMethodWMultiplicity(3, 2, test1, dtest1))

print(newtonsMethod(5, test2, dtest2))
print(newtonsMethodWMultiplicity(5, 3, test2, dtest2))