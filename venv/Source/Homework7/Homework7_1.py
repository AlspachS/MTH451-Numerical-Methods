# Problem 6.3:

# a. Write down the system of nine equations for the nine unknowns:
# (b0, b1, b2, c0, c1, c2, d0, d1, d2) for the Natural Cubic Spline
# through the data points:
#
#       S = {(−1, 4), (4, −2), (7, 9), (10, −1)}
#
# Then use Python’s solve command to solve this system.

# b. Copy our in-class program spline2bal, rename it spline3, and modify
# it so that it takes data vectors x and y, and returns the bi, ci, and di
# coefficients of the Natural Cubic Spline interpolating that data. It
# should also produce a red graph of the spline passing through the data
# points. (The data points should be marked with blue circles.)
# Check your program using the data from part(a).
# Note that the matrix A will have dimensions 3(n−1)×3(n−1) and the
# vector B have a length of 3(n − 1). When constructing A and B recall
# that there will be:
#       • n − 1 equations for continuity.
#       • n − 2 equations for smoothness.
#       • n − 2 equations for concavity smoothness.
#       • 2 equations for the “natural” condition on the endpoints:
#           s``(x0) = 0 = s``(xn).

# c. Test your program on the data from problem 6.1(a). Include the spline
# coefficients and the graph.

from numpy import zeros, linspace
from numpy.linalg import solve
from matplotlib.pyplot import plot, show

def spline3nat(x, y):
    n = len(x)
    b = zeros(n-1)
    c = zeros(n-1)
    d = zeros(n-1)
    A = zeros((3*(n-1), 3*(n-1)))
    B = zeros(3*(n-1))

    for i in range(0, n - 1):
        A[i, i] = (x[i + 1] - x[i])
        A[i, (n - 1) + i] = (x[i + 1] - x[i]) ** 2
        A[i, 2*(n-1)+i] = (x[i+1]-x[i])**3
        B[i] = y[i + 1] - y[i]

    # Smooth at internal endpoints: n-2 equ’s
    for i in range(0, n - 2):
        A[(n - 1) + i, i] = 1
        A[(n - 1) + i, i + 1] = -1
        A[(n - 1) + i, (n - 1) + i] = 2 * (x[i + 1] - x[i])
        A[(n-1)+i, 2*(n-1)+i] = 3*(x[i+1] - x[i])**2

    A[(n - 1) + (n - 2), (n-1)] = 2

    #run loop for one extra to fill in the two spots needed in the last row (natural conditions)
    for i in range(0, n - 1):
        A[2*(n - 1) + i, (n-1)+i] = 2
        A[2*(n - 1) + i, (n-1)+i + 1] = -2
        A[2*(n - 1) + i, 2*(n - 1) + i] = 6 * (x[i + 1] - x[i])

    # Then clear the extra space set in the loop to zero
    A[(3*(n-1)-1), (n-1)+(n-2)] = 0

    z = solve(A, B)
    b[:] = z[0 : n-1]
    c[:] = z[n-1 : 2*(n-1)]
    d[:] = z[2*(n-1) : 3*(n-1)]


    #Plot spline
    for i in range(0,n-1):
        t = linspace(x[i],x[i+1],20)
        s = y[i] + b[i]*(t-x[i])+c[i]*(t-x[i])**2 + d[i] * (t - x[i])**3
        plot(t,s,'red')

    #Plot Data for reference
    plot(x,y,'bo')
    show()
    return b, c, d

ex = [-1 ,4 ,7, 10]
wy = [4, -2, 9, -1]
print(spline3nat(ex, wy))

x = [-2, 2, 4, 5, 7]
y = [3, -1, 8, 6, -10]
print(spline3nat(x, y))
