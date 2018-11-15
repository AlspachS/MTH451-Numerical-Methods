# Problem 1.8
#
# Write a function for the following situation:
#       Arguments: The leading and final coefficients of a polynomial function you
#                   will call from within the method.
#       Purpose: Use the rational zeros theorem to produce a list of potential zeros
#                   and test them to see if they are a zero of the polynomial function.
#       Returns: The rational zeros of the polynomial function. Returns ”None” if
#                   there are no rational zeros

import math

def listFindDivisors(intGiven):
    """
    Finds all the divisors of a number
    :param intGiven: The number to find the divisors of.
    :return:
    """
    divisors  = []

    for i in range(1, math.ceil(math.sqrt(intGiven) + 1)):
        if intGiven % i == 0:
            divisors.append(i)
            if i != intGiven//i:    # Prevent the inclusion of duplicate numbers when intGiven is a square number.
                divisors.append(intGiven//i)

    divisors.sort()    # Divisors are added in pairs, so sort to make it pretty
    return divisors

# ===================================================================================
#   Test functions for listRationalZeros function
# ===================================================================================
def poly1(x):
    return (8*x**4) + (2*x**3) + (45*x**2) + (12*x**1) - (18*x**0)

def poly2(x):
    return (2*x**3) + (1*x**1) - (1*x**0)

def poly3(x):
    return (1*x**3) - (7*x**1) + (6*x**0)

def poly4(x):
    return (3*x**3) - (5*x**2) + (5*x**1) - (2*x**0)

def listRationalZeros(poly, q, p):
    """
    Finds the rational zeros of a function using the rational roots theorem
    :param poly: Test function to find rational roots of.
    :param q:
    :param p:
    :return:
    """
    qFactors = listFindDivisors(q)
    pFactors = listFindDivisors(p)
    possibleZeros = list(set([p/q for p in pFactors for q in qFactors if math.gcd(p, q) == 1]))
    zeros = [zero for zero in possibleZeros if math.isclose(poly(zero), 0, abs_tol=1e-5)]
    zeros += [-zero for zero in possibleZeros if math.isclose(poly(-zero), 0, abs_tol=1e-5)]

    if len(zeros) == 0:
        zeros = None
    return zeros

print(listRationalZeros(poly1, 8, 18))
print(listRationalZeros(poly2, 2, 1))
print(listRationalZeros(poly3, 1, 6))
print(listRationalZeros(poly4, 3, 2))