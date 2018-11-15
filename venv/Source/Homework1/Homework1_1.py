# Problem 1.1:
#
# The binary expansion of 1/7 is (0.001001001 . . .)base 2 (repeating).

# a) Assuming Python also stores 1/7 with 54 digits, how many applications of
# the operation: x = 8*(x - 1/8) would have to be applied before x was no
# longer a fraction? (Recall that 1/8 = (0.001)base 2, while multiplying by 8 moves
# the binary “decimal point” three places to the right.)

# b) Verify your answer to part a by writing a short Python function called
# strange17, taking n as its argument, which applies this operation to 1/7
# n times and returns the result.


def strange17(n):
    """
    Applies operations to a float to examine machine error
    :param n: The number of times to appy the operations
    :return:
    """
    x = 1/7

    for index in range(0, n):
        x = 8*(x - 1/8)

    return x


for index in range(0, 23):
    print("{:3d}:  {}".format(index, strange17(index)))
