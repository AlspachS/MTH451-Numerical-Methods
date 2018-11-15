# 3.)

# From the last homework in class (and from class if you were there), we produced the code for a
# “Natural Cubic” Splines. Splines that are built into different systems use different end conditions (for
# example, MATLAB uses splines with non-a-knot conditions). For this problem, adapt your code on cubic
# splines to change the given conditions to meet:

#       s’(x0) = y’ = s’(xm)

# (The slopes on the ends of the function must match and be constant)
# This will mean changing the two lines in the code that currently set s’’ = 0 at the ends.

from numpy import zeros, linspace, array
from numpy.linalg import solve
from matplotlib.pyplot import plot, show


def spline3nat(x, y):
    n = len(x)
    b = zeros(n - 1)
    c = zeros(n - 1)
    d = zeros(n - 1)
    A = zeros((3 * (n - 1), 3 * (n - 1)))
    B = zeros(3 * (n - 1))

    # Continuous at right endpoints: n-1 equ's
    for i in range(0, n - 1):
        A[i, i] = (x[i + 1] - x[i])
        A[i, (n - 1) + i] = (x[i + 1] - x[i]) ** 2
        A[i, 2 * (n - 1) + i] = (x[i + 1] - x[i]) ** 3
        # Set up Y matrix at the same time
        B[i] = y[i + 1] - y[i]

    # Smooth at internal endpoints: n-2 equ’s
    for i in range(0, n - 2):
        A[(n - 1) + i, i] = 1
        A[(n - 1) + i, i + 1] = -1
        A[(n - 1) + i, (n - 1) + i] = 2 * (x[i + 1] - x[i])
        A[(n - 1) + i, 2 * (n - 1) + i] = 3 * (x[i + 1] - x[i]) ** 2

    # Special row
    A[(n - 1) + (n - 2), 0] = 1

    # Concavity at internal endpoints: n-2 equ's
    for i in range(0, n - 2):
        A[2 * (n - 1) + i, (n - 1) + i] = 2
        A[2 * (n - 1) + i, (n - 1) + i + 1] = -2
        A[2 * (n - 1) + i, 2 * (n - 1) + i] = 6 * (x[i + 1] - x[i])

    # Special row
    A[3 * (n - 1) - 1, 0] = 1
    A[3 * (n - 1) - 1, (n-2)] = -1
    A[3 * (n - 1) - 1, (n-1)+(n-2)] = -2*(x[n-1] - x[n-2])
    A[3 * (n - 1) - 1, (n-1)+(n-1)+(n-2)] = -3*(x[n-1] - x[n-2])**2


    # A[3 * (n - 1) - 1, 3 * (n - 1) - 1] = 6 * (x[n - 1] - x[n - 2])

    # A[3 * (n - 1) - 1, (n - 1) + (n - 2)] = 2
    # A[3 * (n - 1) - 1, 3 * (n - 1) - 1] = 6 * (x[n - 1] - x[n - 2])

    z = solve(A, B)
    b[:] = z[0: n - 1]
    c[:] = z[n - 1: 2 * (n - 1)]
    d[:] = z[2 * (n - 1): 3 * (n - 1)]

    # Plot spline
    for i in range(0, n - 1):
        t = linspace(x[i], x[i + 1], 20)
        s = y[i] + b[i] * (t - x[i]) + c[i] * (t - x[i]) ** 2 + d[i] * (t - x[i]) ** 3
        plot(t, s, 'red')

    # Plot Data for reference
    plot(x, y, 'bo')
    show()
    return b, c, d


x = array([1, 3, 4, 6])
y = array([2, 4, 1, 3])
print(spline3nat(x, y))
