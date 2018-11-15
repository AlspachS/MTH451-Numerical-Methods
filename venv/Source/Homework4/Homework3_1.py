# Problem 3.1:
#
# Consider f(x) = x**(2/3)
#
# a) Find the ﬁrst and second Taylor polynomials, p1 and p2, for f with x0 = 1.
#
# b) Find ξ so that the conclusion of Taylor’s Theorem is satisﬁed for x0 = 1,
#     x = 1.5, and n = 2.
#
# c) Use Python to plot f, p1, and p2. Choose scales on your axes so that the
# shapes of the diﬀerent graphs are evident. The graphs should use diﬀerent
# linestyles and colors, and there should also be a legend. You need not
# submit your code, just the final graph.

import numpy, matplotlib.pyplot as mathplot, matplotlib.patches as Patch

x = numpy.linspace(0, 3)
mathplot.title('x**(2/3) with Taylor Polynomials')
mathplot.xlabel('X values')
mathplot.ylabel('Y values')
L1 = Patch.Patch(color='black',label='f(x) = x**(2/3)')
L2 = Patch.Patch(color='green',label='P1 = (1/3) + (2/3)*x')
L3 = Patch.Patch(color='red',label='P2 = (2/9) + (8/9)*x -(1/9)*x**2')
mathplot.legend(handles=[L1,L2,L3],loc='upper left')

f = x**(2/3)
tp1 = (1/3) + (2/3)*x
tp2 = (2/9) + (8/9)*x -(1/9)*x**2

mathplot.plot(x, f, color='black')
mathplot.plot(x, tp1, color='green', linestyle=':')
mathplot.plot(x, tp2, color='red', linestyle='--')
mathplot.show()
