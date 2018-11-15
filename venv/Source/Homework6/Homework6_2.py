# Problem 5.2

# Consider the IVP y` = t**2−y−2, y(−2) = 0 which has the exact
# solution y(t) = t**2 − 2t − 8e**(−t−2).  Produce a single Python plot
# for −2 ≤ t ≤ 3 which shows:
# • The Euler approximation for n = 10 in blue
# • The Modified Euler approximation for n = 10 in red
# • The actual solution (with enough points that it appears smooth) in green
# • Including a legend with the three different plots labeled correctly
# Include the code and the graph in your write-up.

import numpy
import matplotlib.pyplot

def euler(t0, tn, n, y0, f):
    h = abs(tn-t0)/n
    t = numpy.linspace(t0, tn, n+1)
    y = numpy.zeros(n+1)
    y[0] = y0
    for i in range(0, n):
        y[i+1] = y[i] + h*f(t[i], y[i])
    return y, t


def modeuler(t0, tn, n, y0, f):
    h = abs(tn-t0)/n
    t = numpy.linspace(t0, tn, n+1)
    y = numpy.zeros(n+1)
    y[0] = y0
    for i in range(0, n):
        ym = y[i] + h/2*f(t[i], y[i])
        y[i+1] = y[i] + h*f(t[i] + h/2, ym)
    return y, t

ey, t = euler(-2, 3, 10, -2, lambda t,y:(t**2)-y-2)
mey, t = modeuler(-2, 3, 10, -2, lambda t,y:(t**2)-y-2)

#Both of these work
# actual = list(map(lambda t: (t**2) - 2*t - 8*numpy.e**(-t-2), numpy.linspace(-2, 3)))
actual = [(t**2) - 2*t - 8*numpy.e**(-t-2) for t in numpy.linspace(-2,3)]

matplotlib.pyplot.plot(t, ey, color='blue')
matplotlib.pyplot.plot(t, mey, color='red')
matplotlib.pyplot.plot(numpy.linspace(-2,3), actual, color='green')
matplotlib.pyplot.show()