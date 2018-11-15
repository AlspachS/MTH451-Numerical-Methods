# Problem 6.4:
#
# For the data set:
#
#       S = {(1, −8), (4, −1), (8, 2), (15, 3)}

# a. Find the least squares regression line.
# b. Find the least squares regression parabola.

from numpy import zeros, linspace
from numpy.linalg import solve
from matplotlib.pyplot import plot, show

def leastSquaresLinear(x, y):
    n = len(x)
    r = zeros(2)
    b = zeros(2)
    A = zeros((2,2))

    sumx2 = sum([xi**2 for xi in x])
    sumxy = 0
    for i in range(0,n):
        sumxy += x[i] * y[i]

    A[0, 0] = n
    A[0, 1] = sum(x)
    A[1, 0] = sum(x)
    A[1, 1] = sumx2

    r[0] = sum(y)
    r[1] = sumxy

    b = solve(A, r)

    t = linspace(min(x) - 1, max(x) + 1, 50)
    sol = sum([b[i]*t**i for i in range(0, 2)])

    plot(t, sol, 'green')
    plot(x, y, 'bo')
    show()

    return b


def leastSquaresParabolic(x, y):
    n = len(x)
    r = zeros(3)
    b = zeros(3)
    A = zeros((3,3))

    for i in range(0, n-1):
        for j in range(0, n-1):
            A[i, j] = sum([xi**(i+j) for xi in x])

    for i in range(0, n-1):
        r[i] = sum([x[j]**i * y[j] for j in range(0,n)])

    b = solve(A, r)

    t = linspace(min(x) - 1, max(x) + 1, 50)
    plot(t, b[0] + b[1]*t + b[2]*t**2, 'green')
    plot(x, y, 'bo')
    show()

    return b

def leastSquaresGeneral(x, y, order):
    r = zeros(order)
    n = len(x)
    b = zeros(order)
    A = zeros((order,order))

    for i in range(0, order):
        for j in range(0, order):
            A[i, j] = sum([xi**(i+j) for xi in x])

    for i in range(0, order):
        r[i] = sum([x[j]**i * y[j] for j in range(0,n)])

    b = solve(A, r)

    t = linspace(min(x) - 1, max(x) + 1, 50)

    plot(t, sum([b[i]*t**i for i in range(0, order)]), 'green')
    plot(x, y, 'bo')
    show()

    return b


ex = [1,4,8,15]
wy = [-8,-1,2,3]
leastSquaresGeneral(ex, wy, 2)
leastSquaresGeneral(ex, wy, 3)