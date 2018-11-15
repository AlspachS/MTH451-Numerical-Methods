# Take Home Test Problem 2
#
# In matrix algebra, finding the dominant eigenvalue and eigenvector is a big deal.
# Review the notes from: http://nptel.ac.in/courses/111107062/module3/lecture1/lecture1.pdf
# After reviewing these notes, produce code that will do the following:
#
# 1.) Accept a square matrix of arbitrary size
# 2.) Apply the power method to calculate the dominant eigenvalue of a matrix, accurate to
#       two decimal places.
# 3.) Return the eigenvalue and eigenvector calculated.

from numpy import ones, sqrt, abs, array, reshape
import numpy.linalg


def EiganValandVec(A, startingEstimate):
    if A.shape[0] != A.shape[1]:  # Make sure A is square
        raise ValueError("Improper Dimensions")
    if len(startingEstimate) != A.shape[0]:
        raise ValueError("Vector and Estimate must have the same number of rows")
    startingEstimate = reshape(startingEstimate, (A.shape[0], 1))

    stopping = False
    old = 0
    while not stopping:
        dotOp = A.dot(startingEstimate)
        new = max(dotOp)
        startingEstimate = dotOp / new
        if abs(old - new) < 0.01:
            stopping = True
        old = new

    return old, startingEstimate

print(EiganValandVec(array([[4, -5], [2, -3]]), [1,0]))
print(EiganValandVec(array([[0, 11, -5],[-2, 17, -7],[-4,26,-10]]), [1,1,1]))