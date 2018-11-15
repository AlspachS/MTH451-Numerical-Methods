# Apply the VanderMonte Method to find the polynomial of lowest order that
# goes through the points:  {(0,0),(1,3),(-2,5),(5,4), (-4,6)}
#
# Graph the resulting polynomial and report it's equation.

import numpy, matplotlib.pyplot

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

ex = numpy.array([1, -2, 5, -4, 0])
wy = numpy.array([3, 5, 4, 6, 0])

v = numpy.array([[a**x for x in range(len(ex) - 1, -1, -1)] for a in ex])
v = numpy.insert(v, len(v), wy, 1)
print(v)

print(GE(v))



t = numpy.linspace(-10, 10, 5)
matplotlib.pyplot.plot(t, GE(v))
matplotlib.pyplot.plot(ex, wy,'o')
matplotlib.pyplot.show()