# Problem 1.5:

# Write a function for the following situation:
#       Arguments:  A single integer
#       Purpose:    Create a list of all divisors for the given integer
#       Returns:    The list of all divisors of the given integer

from math import ceil, sqrt

def listFindDivisors(intGiven):
    """
    Finds all the divisors of a number
    :param intGiven: The number to find the divisors of.
    :return:
    """
    divisors  = []

    for i in range(1, ceil(sqrt(intGiven) + 1)):
        if intGiven % i == 0:
            divisors.append(i)
            if i != intGiven//i:    # Prevent the inclusion of duplicate numbers when intGiven is a square number.
                divisors.append(intGiven//i)

    divisors.sort()    # Divisors are added in pairs, so sort to make it pretty
    return divisors

print(listFindDivisors(180000000000000000000000000000000000000000000))