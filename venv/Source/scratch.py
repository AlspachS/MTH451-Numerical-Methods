# from math import pi, cos, sqrt, ceil, exp
# import matplotlib.pyplot as mathplot
# import numpy
# from scipy import matrix

# print(cos(pi/4))
# print(16*(0.2-3/16))
#
# print(matrix([[1,2],[3,4]]))

# def strEvenOrOdd(intNumber):
#     '''
#     Returns a string indicating whether the number passed in is odd or even.
#     :param intNumber: The number to determine whether even or odd
#     :return:
#     '''
#     ret = 'Odd'
#     if intNumber % 2 == 0:
#         ret = 'Even'
#     return(ret)
#
# print(strEvenOrOdd(intNumber=-3))
# print(strEvenOrOdd(intNumber=-2))
# print(strEvenOrOdd(intNumber=-1))
# print(strEvenOrOdd(intNumber=0))
# print(strEvenOrOdd(intNumber=1))
# print(strEvenOrOdd(intNumber=2))
# print(strEvenOrOdd(intNumber=3))

# def listMaxLimit(listIntegers, intMaxVal):
#     '''
#     Loops through a list and creates a new list of values less than a value.
#     :param listIntegers: A list of integers to check
#     :param intMaxVal: The value to check against
#     :return:
#     '''
#     ret = []
#     for index in listIntegers:
#         if index < intMaxVal:
#             ret.append(index)
#     return ret

# print(listMaxLimit([1,2,7,9,11,14,22], 11))

# def listCommonFactors(intFirst, intSecond):
#     commonFactors = []
#     larger = intFirst
#     smaller = intSecond
#     if intFirst < intSecond:
#         larger = intSecond
#         smaller = intFirst
#     for i in (range(1, ceil(sqrt(larger)))):
#         if larger % i == 0:
#             if smaller % i == 0:
#                 commonFactors.append(i)
#                 commonFactors.append(intFirst // i)
#
#     # print(commonFactors)


# listCommonFactors(20, 32)

# print(range(1, ceil(sqrt(20))))

# def f(x):
#     return exp(x) + x - 2

# print(f(1))


# def bisectOnce(a, b):
#     mid = (a+b) / 2
#     midEvaled = f(mid)
#     if midEvaled > 0:
#         b = mid
#     elif midEvaled < 0:
#         a = mid
#     else:
#         # found the zero
#         pass
#     print(a, b)
#     return(a, b)

# bisectOnce(0, 1)
# bisectOnce(0, 0.5)

# def bisectNTime(a, b, n):
#     for index in range(0, n):
#         a, b = bisectOnce(a, b)
#     error = abs(b - a)/2
#     return(a, b, error)

# print(bisectNTime(0, 1, 10))

# def oneSecMethStep(a, b, tol=0.01, maxItter = 1000):
#     c = b - (f(b)*(b - a)) / (f(b) - f(a))
#     a = b
#     b = c
#     itter = 1
#     while abs(f(c)) > tol and itter < maxItter:
#         c = b - (f(b)*(b - a)) / (f(b) - f(a))
#         a = b
#         b = c
#         itter += 1
#     return c, itter

# print(oneSecMethStep(0, 2, 0.00000001))

# def df(x):
#     return exp(x) + 1

# def newtonsMethod(a, tol=0.001, maxIter=100):
#     i = 0
#     while abs(f(a)) > tol and i < maxIter:
#         i += 1
#         a = a - f(a)/df(a)
#
#     return(a, f(a), i)

# print(newtonsMethod(12))

# Taylor's Series

# f(x) = f(xnaught) + f`(xnaught)*(x - xnaught) + (f``(xnaught)/2) * (x - xnaught)**2
#        f



# x = numpy.linspace(-3, 3, 50)
# mathplot.plot(x, numpy.exp(x))
# mathplot.title('Exponential')
# mathplot.xlabel('X values')
# mathplot.ylabel('Y values')
# mathplot.show()
#
#
# mathplot.plot(x, numpy.exp(x), color='blue')
# tp1 = 1 + x
# mathplot.plot(x, tp1, color='black', linestyle=':')
# tp2 = None
# mathplot.plot(x, tpw, color='red', linestyle='--')

# def f(x):
#     return (numpy.exp(x))
#
# def df(x):
#     return (numpy.exp(x))

# def FFDD(x, h=0.001):
#     return (f(x+h) - f(x)) / h
#
# def FBDD(x, h=0.001):
#     return (f(x) - f(x-h)) / h

# def FCDD(x, h=0.001):
#     return (f(x+h) - f(x-h)) / (2*h)
#
# def printTable(x, n):
#     for i in range(0, n):
#         h = 10**(-i-1)
#         a = FFDD(x, h)
#         b = FBDD(x, h)
#         c = FCDD(x, h)
#         ea = a - df(x)
#         eb = b - df(x)
#         ec = c - df(x)
#         print("{:03.5f}\t{:03.5f}\t{:03.5f}\t{:03.5f}\t{:03.5f}\t{:03.5f}\t{:03.5f}".format(h, a, ea, b, eb, c, ec ))

# printTable(1, 5)

# def SCDD(x, h):
#     return (f(x + h) - 2*f(x) + f(x-h)) / h**2
#
# def printresults(x, n):
#     for i in range(0, n):
#         h = 10**(-i-1)
#         c = SCDD(x,h)
#         ec = c - df(x)
#         print(h, '\t', round(c, 4), '\t', ec)

# printresults(1, 5)

# import math
# def f(x):
#     return math.log(x)
#
# def df(x):
#     return 1/x
#
# def F(x):
#     return x*math.log(x) - x

# def trapazoidal(a, b, n):
#     h = abs(a-b)/n
#     heights = f(a) + f(b)
#     for i in range(1, n-1):
#         heights += 2*f(a + i*h)
#     area = heights * (h/2)
#     ex = F(b) - F(a)
#     return area, area-ex

# def trapazoidal(a, b, n):
#     h = abs(a-b)/n
#     heights = 0
#     x = a
#
#     area = (h/2)*(f(a) + f(b))
#     for i in range(1, n):
#         x += h
#         heights += f(x)
#
#     area = area + heights * h
#     ex = F(b) - F(a)
#     return area, area-ex

# for i in range(0,6):
#     A, E = trapazoidal(1, 2, 10**i)
#     print(10**i, E)

# def evenOrOdd(n):
#     return(n%2 == 0)

#
# import math
# def f(x):
#     return math.log(x)
#
# def df(x):
#     return 1/x
#
# def F(x):
#     return x*math.log(x) - x
#
# def simpsons(a, b, n):
#     if( n%2 != 0):
#         raise ValueError("N needs to be even")
#
#     h = abs(a - b) / n
#     sum1 = sum2 = 0
#
#     for k in range(1, int(n/2+1)):
#         sum1 = sum1 + f(a + h + 2*h*(k-1))
#
#     for j in range(1, int(n/2)):
#         sum2 = sum2 + f(a + 2*h*j)
#
#     area = (h/3)*(f(a) + f(b) + 4*sum1 + 2*sum2)
#     ex = F(b) - F(a)
#     return area, area - ex
#
#
#
# for n in range(1, 6):
#     A, E = simpsons(1, 2, 10**n)
#     print(10**n, E)
#
# for i in range(0, 10):
#     print(i%5)  # mod X makes X number of groups
#
# import matplotlib.pyplot
# import numpy
#
# def test(t, y):
#     return -2*y
#
# def testtrue(t):
#     return 3*numpy.exp(-2*t)
#
# def dttest(t,y):
#     return 0
#
# def dytest(t,y):
#     return -2
#
# def test2(t, y):
#     return -2*numpy.sin(y**2)*(1/(t+1)) + (1/y)
#
# def test3(t, y):
#     return 3*numpy.sin(t) - y
#
# def dttest3(t, y):
#     return 3*numpy.cos(t)
#
# def dytest3(t, y):
#     return -1
#
# def euler(t0, tn, n, y0, f):
#     h = abs(tn-t0)/n
#     t = numpy.linspace(t0, tn, n+1)
#     y = numpy.zeros(n+1)
#     y[0] = y0
#     for i in range(0, n):
#         y[i+1] = y[i] + h*f(t[i], y[i])
#     return y, t
#
# def taylors(t0, tn, n, y0, f, dft, dfy):
#     h = abs(tn-t0)/n
#     t = numpy.linspace(t0, tn, n+1)
#     y = numpy.zeros(n+1)
#     y[0] = y0
#     for i in range(0, n):
#         y[i+1] = y[i] + h*f(t[i], y[i]) + ((h**2)/2)*(dft(t[i], y[i]) + dfy(t[i], y[i])*f(t[i], y[i]))
#     return y, t
#
# def modeuler(t0, tn, n, y0, f):
#     h = abs(tn-t0)/n
#     t = numpy.linspace(t0, tn, n+1)
#     y = numpy.zeros(n+1)
#     y[0] = y0
#     for i in range(0, n):
#         ym = y[i] + h/2*f(t[i], y[i])
#         y[i+1] = y[i] + h*f(t[i] + h/2, ym)
#
#     return y, t
#
# ey, t = euler(0, 10, 30, 3, test3)
# ty, t = taylors(0, 10, 30, 3, test3, dttest3, dytest3)
# mey, t = modeuler(0, 10, 30, 3, test3)
# matplotlib.pyplot.plot(t, ey, color='blue')
# matplotlib.pyplot.plot(t, ty, color='green')
# matplotlib.pyplot.plot(t, mey, color='black')
# matplotlib.pyplot.show()
# import numpy
#
# test = numpy.matrix([[-1, 2, 3/5, 4, 16],[-4, 5, 6, 7, -8],[7, 8, 9, 10, 0], [2, 4, 6, 8, 10]])
#
# def GE(x):
#     x = x.astype(float64)
#     col = numpy.size(x, 1)
#     row = numpy.size(x, 0)
#     sol = numpy.zeros(row)
#
#     if col != (row + 1):
#         return ('Improper Dimensions')
#
#     for i in range(0, col-1):
#         for j in range(0, row):
#             if( i != j):
#                 x[j] = x[j,i]*x[i] - x[i,i]*x[j]
#                 print(x)
#
#     for j in range(0, row):
#         if x[j, j] == 0:
#             return ('Under Determined System')
#         x[j] = x[j] / x[j, j]
#
#     sol = x[:,col-1]
#
#     return sol
#
#
# print(GE(test))

# import pprint, numpy

# def mult_matrix(M, N):
#     """Multiply square matrices of same dimension M and N"""
#
#     # Converts N into a list of tuples of columns
#     tuple_N = zip(*N)
#
#     # Nested list comprehension to calculate matrix multiplication
#     return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

# def pivot_matrix(M):
#     """Returns the pivoting matrix for M, used in Doolittle's method."""
#     m = len(M)
#
#     # Create an identity matrix, with floating point values
#     id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]
#
#     # Rearrange the identity matrix such that the largest element of
#     # each column of M is placed on the diagonal of of M
#     for j in range(m):
#         row = max(range(j, m), key=lambda i: abs(M[i][j]))
#         if j != row:
#             # Swap the rows
#             id_mat[j], id_mat[row] = id_mat[row], id_mat[j]
#
#     return id_mat
#
# def lu_decomposition(A):
#     """Performs an LU Decomposition of A (which must be square)
#     into PA = LU. The function returns P, L and U."""
#     n = len(A)
#
#     # Create zero matrices for L and U
#     L = [[0.0] * n for i in range(n)]
#     U = [[0.0] * n for i in range(n)]
#
#     # Create the pivot matrix P and the multipled matrix PA
#     P = pivot_matrix(A)
#     PA = numpy.matmul(P, A)
#
#     # Perform the LU Decomposition
#     for j in range(n):
#         # All diagonal entries of L are set to unity
#         L[j][j] = 1.0
#
#         for i in range(j+1):
#             s1 = sum(U[k][j] * L[i][k] for k in range(i))
#             U[i][j] = PA[i][j] - s1
#
#         for i in range(j, n):
#             s2 = sum(U[k][j] * L[i][k] for k in range(j))
#             L[i][j] = (PA[i][j] - s2) / U[j][j]
#
#     return (P, L, U)
#
#
# A = [[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]
# P, L, U = lu_decomposition(A)
#
# print("A:")
# pprint.pprint(A)
#
# print ("P:")
# pprint.pprint(P)
#
# print( "L:")
# pprint.pprint(L)
#
# print ("U:")
# pprint.pprint(U)

# import numpy, matplotlib.pyplot
#
# def NewtonsDD(x, y):
#     n = len(x)
#     M = numpy.zeros((n,n))
#     M[:,0] = y[:]
#     for j in range(1, n):
#         for i in range(j,n):
#             M[i, j] = (M[i, j-1] - M[i-1, j-1])/(x[i]-x[i-j])
#     a = min(x) - 1
#     b = max(x) + 1
#     t = numpy.linspace(a, b, 100)
#     p = numpy.zeros(100) + M[n - 1, n - 1]
#     for i in range(n - 2, -1, -1):
#         p = p * (t - x[i]) + M[i, i]
#     matplotlib.pyplot.plot(t, p,'green')
#     matplotlib.pyplot.title('Interpolating Polynomial')
#     # Plot data points for reference
#     matplotlib.pyplot.plot(x, y,'o')
#     matplotlib.pyplot.show()
#     return M
#
# x = numpy.array([0, 2, 3, 5])
# y = numpy.array([1, 5, 0, 8])
# print(NewtonsDD(x, y))

# from numpy import zeros, array, linspace
# from numpy.linalg import solve
# from matplotlib.pyplot import plot, title, show

# def spline1(x, y):
#     b = numpy.zeros(len(x)-1)
#     for i in range(0, len(x)-1):
#         b[i] = (y[i+1] - y[i]) / (x[i+1]-x[i])
#     return b
#
# x = numpy.array([1, 3, 4, 6])
# y = numpy.array([2, 4, 1, 3])

# def spline2(x, y, m0):
#     n = len(x)
#     b = zeros(n-1)
#     c = zeros(n-1)
#     A = zeros((2*(n-1), 2*(n-1)))
#     B = zeros(2*(n-1))
#
#     for i in range(0, n - 1):
#         A[i, i] = (x[i + 1] - x[i])
#         A[i, (n - 1) + i] = (x[i + 1] - x[i]) ** 2
#         B[i] = y[i + 1] - y[i]
#
#     # Smooth at internal endpoints: n-2 equ’s
#     for i in range(0, n - 2):
#         A[(n - 1) + i, i] = 1
#         A[(n - 1) + i, i + 1] = -1
#         A[(n - 1) + i, (n - 1) + i] = 2 * (x[i + 1] - x[i])
#
#     # Set initial slope: 1 equ
#     A[(n - 1) + (n - 2), 0] = 1
#     B[(n - 1) + (n - 2)] = m0
#
#     z = solve(A, B)
#     b[:] = z[0 : n-1]
#     c[:] = z[n-1 : 2*(n-1)]
#
#     print('b = ', b)
#     print('c = ', c)
#
#     #Plot spline
#     for i in range(0,n-1):
#         t = linspace(x[i],x[i+1],20)
#         s = y[i] + b[i]*(t-x[i])
#     plot(t,s,'black')
#
#     #Plot Data for reference
#     plot(x,y,'bo')
#     return A, B
#
# x = array([1, 3, 4, 6])
# y = array([2, 4, 1, 3])
# print(spline2(x, y, 2))

# from numpy import zeros
#
# def spline3nat(x, y):
#     n = len(x)
#     b = zeros(n-1)
#     c = zeros(n-1)
#     d = zeros(n-1)
#     A = zeros((3*(n-1), 3*(n-1)))
#     B = zeros(3*(n-1))
#
#     for i in range(0, n - 1):
#         A[i, i] = (x[i + 1] - x[i])
#         A[i, (n - 1) + i] = (x[i + 1] - x[i]) ** 2
#         A[i, 2*(n-1)+i] = (x[i+1]-x[i])**3
#         B[i] = y[i + 1] - y[i]
#
#     # Smooth at internal endpoints: n-2 equ’s
#     for i in range(0, n - 2):
#         A[(n - 1) + i, i] = 1
#         A[(n - 1) + i, i + 1] = -1
#         A[(n - 1) + i, (n - 1) + i] = 2 * (x[i + 1] - x[i])
#         A[(n-1)+i, 2*(n-1)+i] = 3*(x[i+1] - x[i])**2
#
#     A[(n - 1) + (n - 2), (n-1)] = 2
#
#     #run loop for one extra to fill in the two spots needed in the last row (natural conditions
#     for i in range(0, n - 1):
#         A[2*(n - 1) + i, (n-1)+i] = 2
#         A[2*(n - 1) + i, (n-1)+i + 1] = -2
#         A[2*(n - 1) + i, 2*(n - 1) + i] = 6 * (x[i + 1] - x[i])
#
#     A[(3*(n-1)-1), (n-1)+(n-2)] = 0
#
#     z = solve(A, B)
#     b[:] = z[0 : n-1]
#     c[:] = z[n-1 : 2*(n-1)]
#     d[:] = z[2*(n-1) : 3*(n-1)]
#
#
#     #Plot spline
#     for i in range(0,n-1):
#         t = linspace(x[i],x[i+1],20)
#         s = y[i] + b[i]*(t-x[i])+c[i]*(t-x[i])**2 + d[i] * (t - x[i])**3
#         plot(t,s,'black')
#
#     #Plot Data for reference
#     plot(x,y,'bo')
#     show()
#     return b, c, d
#
# x = array([1, 3, 4, 6])
# y = array([2, 4, 1, 3])
# print(spline3nat(x, y)

# import numpy
# import numpy.linalg
# import matplotlib.pyplot
#
# def leastSquares(x, y):
#     n = len(x)
#     r = numpy.zeros(2)
#     b = numpy.zeros(2)
#     A = numpy.zeros((2,2))
#
#     sumx2 = sum([xi**2 for xi in x])
#     sumxy = 0
#     for i in range(0,n):
#         sumxy += x[i] * y[i]
#
#     A[0, 0] = n
#     A[0, 1] = sum(x)
#     A[1, 0] = sum(x)
#     A[1, 1] = sumx2
#
#     r[0] = sum(y)
#     r[1] = sumxy
#
#     b = numpy.linalg.solve(A, r)
#
#     return b
#
#
# ex = [1,2,4,5]
# wy = [3,6,10,9]
# print(leastSquares(ex, wy))

# import numpy
# import numpy.linalg
# import matplotlib.pyplot
#
# def leastSquares(x, y):
#     n = len(x)
#     r = numpy.zeros(3)
#     b = numpy.zeros(3)
#     A = numpy.zeros((3,3))
#
#
#     sumx2 = sum([xi**2 for xi in x])
#     sumxcube = sum([xi**3 for xi in x])
#     sumxfour = sum([xi**4 for xi in x])
#     sumxy = 0
#     sumx2y = 0
#     for i in range(0,n):
#         sumxy += x[i] * y[i]
#         sumx2y += x[i]**2 * y[i]
#
#     A[0, 0] = n
#     A[0, 1] = sum(x)
#     A[0, 2] = sumx2
#     A[1, 0] = sum(x)
#     A[1, 1] = sumx2
#     A[1, 2] = sumxcube
#     A[2, 0] = sumx2
#     A[2, 1] = sumxcube
#     A[2, 2] = sumxfour
#
#     r[0] = sum(y)
#     r[1] = sumxy
#     r[2] = sumx2y
#
#     b = numpy.linalg.solve(A, r)
#
#     t = numpy.linspace(min(x) - 1, max(x) + 1, 50)
#     matplotlib.pyplot.plot(t, b[0] + b[1]*t + b[2]*t**2, 'green')
#     matplotlib.pyplot.plot(x, y, 'bo')
#     matplotlib.pyplot.show()
#
#     return b
#
#
# ex = [1,2,4,5]
# wy = [3,6,10,9]
# print(leastSquares(ex, wy))