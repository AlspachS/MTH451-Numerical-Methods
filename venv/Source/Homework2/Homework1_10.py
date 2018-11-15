# Problem 1.10
# Determining approximations for square roots can be a
# difficult task by hand. Our goal in this problem will be to derive and code a
# numeric method that can approximate the square root of a number.

# a) Let S be the number that we want to take a square root of.
# Then √S = x or perhaps x**2 = S. Obviously, we don’t know what x is so we
# will be off by some error e. i.e. S ≈ (x + e)**2.  Start by partially
# solving for e (and assume e < x). Basically, there will be an isolated e on
# the left hand side of the equation and an additive e on the denominator of
# the right hand side when you stop.

# b) Now, using this calculation, let e go to 0 on the denominator as we
# iterate. x + e ≈ x + ... (replace e with the result from the previous step).
# Algebraically simplify this expression to give us a revised estimate of x.

# c) Write a function for the following situation:
#       Arguments: The number you are trying to take the square root of, an
#                   initial guess of the square root, and the ammount of
#                   acceptable error (i.e. 0.001 for example)
#       Purpose: This function will apply the method derived above to iteratively
#                   approximate the square root of a number to the determined
#                   accuracy.
#       Returns: A vector of all progressive estimates of the square root of the
#                   starting number until you are within the accuracy provided.

# d) Make a table of the iterative results when attempting to estimate the square
# root of two with an initial guess of six and an accuracy of 8 decimal places.
# For the second column of the table, record the error at each itteration. Use
# this information and ”big O” to describe the convergence of this algorithm.

# 6                         -102.0
# 3.1666666666666665        -12.710648148148145
# 1.8991228070175439        -1.5256293856274266
# 1.4761202949637373        -0.13206193265703609
# 1.4155117098049557        -0.002599870778477263
# 1.4142141576301823        -1.1905149261449813e-06
# 1.4142135623732204        -2.505867564059527e-13
# 1.414213562373095

# Convergence is quadratic.

import math

def listSquareRoot(intS, intX, floatE):
    """
    Finds an estimate of a square root using the Babylonian method of estimating
    the square root by including some error in the calculation and iterating
    through the calculation while allowing that error to go to zero.
    :param intS:
    :param intX:
    :param floatE:
    :return:
    """
    guessProgression = [intX]
    error = 1

    while abs(error) > floatE:
        nextX = (intS/intX + intX) / 2
        error = (intS-intX**2) / 2*intX
        print(error)
        guessProgression.append(nextX)
        intX = nextX
    return guessProgression

# print(math.sqrt(8))
# print(listSquareRoot(8, 3, 1e-14))
print(math.sqrt(2))
print(listSquareRoot(2, 6, .00000001))
