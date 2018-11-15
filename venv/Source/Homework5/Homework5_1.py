# Problem 4.3:
#
# Consider the integral
#
#       INTEGRATE 0|2 (5*x**6 − 12*x**5 + 30*x**3 − 90*x**2 + 4*x + 1)dx
#
# a) Use trap to apply the Trapezoid Rule to estimate this integral for
#       n = 10, n = 100, and n = 1000.
#
# b) What is the order of the estimate? How do you know?
#
#        It looks like the error is O(h**4)
#
#           0.09971678571427844
#           0.0009999716667437042
#           0.000009999997104159775
#
# c) Is this behavior surprising? Do you have an explanation? (Hint: Consider
#       the Improved Trapezoid Rule)
#
#       This IS surprising since the Trapezoid rule is
#       typically an O(h**2) method.  The explanation must be related to
#       being able to express the error as a constant involving f`,
#       which reduces the order of the error from h**2, to h**4.
#

import math

def test(x):
    return 5*x**6 - 12*x**5 + 30*x**3 - 90*x**2 + 4*x + 1

def F(x):
    return (5/7)*x**7 - 2*x**6 + (15/2)*x**4 - 30*x**3 + 2*x**2 + x

def trapazoidal(a, b, n, f):
    h = abs(a-b)/n
    area = (h/2)*(f(a) + f(b))
    for i in range(1, n):
        area += f(a + (i*h)) * h
    return area

for i in range(1,4):
    estimate = trapazoidal(0, 2, 10**i, test)
    exact = F(2) - F(0)
    error = estimate - exact
    print(exact, estimate, error, 10**i)