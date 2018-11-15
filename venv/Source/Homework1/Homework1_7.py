# Problem 1.7:
#
# Write a function for the following situation:
#       Arguments:  An integer (x > 1) and a bound near zero.
#       Purpose:    Finds the smallest natural number n such that 1/x^n < bound.
#       Returns:    The number n and the value of 1/x^n

def intfloatSmallestBound(intBase, floatBound):
    """
    Finds the smallest whole number greater than one that causes 1/x^n to evaluate to less than the given bound.
    :param intBase:  x, the base of the exponent
    :param floatBound:  The bound at which to stop calculating
    :return:
    """
    val = 1
    n = 0
    while abs(val) > floatBound:
        val = 1/intBase**n
        if abs(val) < floatBound:
            return n, val
        n += 1

print(intfloatSmallestBound(-3, 0.0000000000001))
print(intfloatSmallestBound(5, 0.0005))
print(intfloatSmallestBound(3, 0.0000000000001))
