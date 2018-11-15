# 1.) Apply your Gaussian elimination code to find the solution to the following problem.
#
#       [[ 3, 2, 1 ],   [x      [1
#        [ 5, 3, 1 ],    y  =    2
#        [ 6, 1, 2 ]]    z]      4]
#
# Submit the code with your implementation.

import numpy

def GE(x):
    x = x.astype(numpy.float64)
    col = numpy.size(x, 1)
    row = numpy.size(x, 0)
    sol = numpy.zeros(row)

    if col != (row + 1):
        return ('Improper Dimensions')

    for i in range(0, col-1):
        for j in range(0, row):
            if( i != j):
                x[j] = x[j,i]*x[i] - x[i,i]*x[j]

    for j in range(0, row):
        if x[j, j] == 0:
            return ('Under Determined System')
        x[j] = x[j] / x[j, j]

    sol = x[:,col-1]

    return sol

# test = numpy.matrix([[-1, 2, 3/5, 4, 16],[-4, 5, 6, 7, -8],[7, 8, 9, 10, 0], [2, 4, 6, 8, 10]])
test = numpy.matrix([[3,2,1,1],[5,3,1,2],[6,1,2,4]])#,[1,2,4]])

print(GE(test))