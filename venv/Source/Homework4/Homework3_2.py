# Problem 3.2:
#
# a) Use the Central Diﬀerence formula to approximate f`(2) for f(x) = ln(x)
# and h = 0.2 and h = 0.1. What sort of reduction in the error do you expect? Why?
#
# b) Use Taylor’s Theorem to show:
#
#         f`(x) = ( f(x+2h) − 8f(x+h) + 8f(x−h) − f(x−2h) / −12h ) + O(h**4)
#
# c) Write a short Python program called C8D which takes x and h as arguments
# and returns the approximation of f`(x) obtained from the rule introduced in
# part(b). It should also print the error between this estimate and the true
# value of f`(x).
#
# d) Use the program from part(c) to approximate f`(2) for f(x) = ln(x)
# with h = 0.2 and h = 0.1.
#
# e) Compare the errors in the previous two parts.

import math

def test1(x):
    return math.log(x)

def dtest1(x):
    return 1 / x

def C8D(function, derivative, x, h=0.001):
    xApprox = (function(x+2*h) - 8*function(x+h) + 8*function(x-h) - function(x-2*h)) / (-12*h)
    print(abs(xApprox - derivative(x)))
    return xApprox


print(C8D(test1, dtest1, 2, 0.2))
print(C8D(test1, dtest1, 2, 0.1))
print(dtest1(2))