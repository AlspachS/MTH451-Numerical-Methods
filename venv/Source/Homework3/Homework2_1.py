# There is a variation on the Bisection Method called the Method of False
# Position. This method also requires that the function be continuous and
# that you have bracketed a zero. However, instead of considering the midpoint
# of the interval at each step, this method takes the x-intercept, xsubi of the
# line from (a,f(a)) through (b,f(b)). As before, xsubi becomes the new left or
# right endpoint of the new, smaller interval depending on whether f(xsubi) is
# positive or negative. However with this method, the interval will not, in
# general, approach zero width. Instead, one of the end points will approach the
# actual zero.

# a. Derive the formula for xsubi:

#   xsubi = a*f(b)−b*f(a) / f(b)−f(a)

# b. Write programs falseposonce and falseposntimes which implement the Method
# of False Position. As in the Bisection Method, the program should return the
# estimated zero and the error. As opposed to the Bisection Method, however, the
# estimated zero should be either the left or right endpoint. We will estimate
# the error as the distance between xsubi and the appropriate endpoint.
#
# c. Test your program by ﬁnding the zero for f(x) = e**x + x − 2. How many
# iterations does it take to get an error less than 10e-4? How does that compare
# to the Bisection Method?

# It took half the iterations to reach the given tolerance for a=0 and b=2.
# Five, instead of ten.

import math

def test1(x):
    return math.exp(x) + x - 2

def falseposonce(f, a, b):
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    return b, c

def falseposntimes(function, a, b, tol=10e-4, maxIter=100):
    itter = 0
    while abs(a - b) > tol and itter < maxIter:
        a, b = falseposonce(function, a, b)
        itter += 1
    return a, b, itter

print(falseposntimes(test1, 0, 5))
