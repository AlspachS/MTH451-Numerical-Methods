# Problem 1.6:

# Write a function for the following situation:
#       Arguments:  A low and high value as well as a test number.
#       Purpose:    Find all numbers between the low and high (non-inclusive) that are
#                       divisible by the test number.
#       Returns:    A list of the numbers that are divisible by the test number within
#                       the open interval and a count of the total numbers.

def listDivisibilityBetween(intLow, intHigh, intDivisor):
    """
    Finds all the numbers between intLow and intHigh that are divisable by intDivisor
    :param intLow: The lower bound
    :param intHigh: The upper bound
    :param intDivisor: The number to divide by
    :return:
    """
    # List comprehension:
    # Creates a new list from an existing list with the new list containing values
    # transformed or filtered from the original list.
    #    [ transform,            range,                  filter/condition
    return [ index for index in range(intLow+1, intHigh) if index % intDivisor == 0 ]


print(listDivisibilityBetween(3, 51, 3))