# Problem 1.9

# Write a function for the following situation:
#       Arguments: Positive integers x,y and a value K
#       Purpose: This function will find all multiples of values x and y that are less
#                   than K.
#       Returns: A single integer that is the sum of all the values that are multiples
#                   of both x and y but less than K.

def intSumMultiples(intX, intY, intMax):
    """
    Finds all the multiples of two numbers, below a certain value, then returns
    the sum of those two sums.
    :param intX:
    :param intY:
    :param intMax:
    :return:
    """
    # return sum([index for index in range(0, intMax, intX)] + [index for index in range(0, intMax, intY)])

    sumIntXMultiples = sum([index for index in range(0, intMax, intX)])
    sumIntYMultiples = sum([index for index in range(0, intMax, intY)])

    return sumIntXMultiples + sumIntYMultiples


print(intSumMultiples(3, 5, 22))